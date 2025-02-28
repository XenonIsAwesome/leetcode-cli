from leet.lang_handlers.handler import LanguageHandler
from pathlib import Path
import os


class PythonHandler(LanguageHandler):
    @property
    def comment(self) -> str:
        return "# "
    
    @property
    def file_ext(self) -> str:
        return "py"
    
    def code_start(self, func_name: str) -> str:
        fmt_func_name = func_name.replace('-', '_').replace(' ', '_').lower()
        return f"""

class Solution:
    @staticmethod
    def {fmt_func_name}():
        # Implement
        ...


if __name__ == \"__main__\":
    Solution.{fmt_func_name}()
"""
    
    def run(self, file_path: Path):
        if os.name == 'nt':
            python_cmd = 'py'
        elif os.name == 'posix':
            python_cmd = '/usr/bin/env python3'
        else:
            raise NotImplementedError(os.name)
        
        os.system(f"{python_cmd} {file_path}")
    