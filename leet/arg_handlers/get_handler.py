import os
from pathlib import Path

from leet import ConfigUtils
from leet.api.alfa_client import AlfaAPIClient
from leet.api.html2text import html2text
from leet.lang_handlers.handler import LanguageHandler
from leet.lang_handlers.factory import LangHandlerFactory

def get_handler(args):
    editor = args.editor
    lang = args.lang
    args_dict = vars(args)
    slug = args_dict["question-slug-or-id"]
    
    lang_handler: LanguageHandler = LangHandlerFactory.get(lang)
    
    question_details = AlfaAPIClient.get_question(slug)
    question_raw = question_details["question"]
    question_text = question_details["link"] + "\n\n" + html2text(question_raw)
    question_slug = question_details["titleSlug"]
    
    leet_path = ConfigUtils()["leet_path"]
    if leet_path:
        leet_path = Path(leet_path).expanduser()
        os.makedirs(leet_path, exist_ok=True)
    
    edit_file = (leet_path or Path.cwd()) / f"{question_slug}.{lang_handler.file_ext}"
    if not edit_file.exists():
        file_content: str = "\n".join([f"{lang_handler.comment}{line}" for line in question_text.split("\n")])
        file_content += lang_handler.code_start(question_slug)
        
        edit_file.write_text(file_content)
    
    edit_file_cmd = f"{editor} {edit_file}"
    os.system(edit_file_cmd)