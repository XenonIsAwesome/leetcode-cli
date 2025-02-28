import os
import json
from pathlib import Path

from leet import ConfigUtils
from leet.api.alfa_client import AlfaAPIClient
from leet.api.html2text import html2text
from leet.lang_handlers.handler import LanguageHandler
from leet.lang_handlers.factory import LangHandlerFactory

def get_handler(args):
    # Args
    editor = args.editor
    lang = args.lang
    args_dict = vars(args)
    slug = args_dict["question-slug-or-id"]
    
    # Question
    question = AlfaAPIClient.get_question(slug)
    question_text = question["question"]
    question_slug = question["titleSlug"]
    question_id = question["questionFrontendId"]
    
    fmt_question_text = question["link"]
    fmt_question_text += "\n\n"
    fmt_question_text += html2text(question_text)

    # Files
    leet_path = ConfigUtils()["leet_path"]
    if leet_path:
        leet_path = Path(leet_path).expanduser()
    else:
        leet_path = Path.cwd()
    
    leet_code_path = leet_path / "code" / question_id
    os.makedirs(leet_code_path, exist_ok=True)
    
    question_json_file: Path = leet_code_path / f"{question_slug}.json"
    if not question_json_file.exists():
        question_json_file.write_text(json.dumps(question, indent=4))
    
    lang_handler: LanguageHandler = LangHandlerFactory.get(lang)
    edit_file = leet_code_path / f"{question_slug}.{lang_handler.file_ext}"
    if not edit_file.exists():
        file_content: str = "\n".join([f"{lang_handler.comment}{line}" for line in fmt_question_text.split("\n")])
        file_content += lang_handler.code_start(question_slug)
        
        edit_file.write_text(file_content)
    
    edit_file_cmd = f"{editor} {edit_file}"
    os.system(edit_file_cmd)