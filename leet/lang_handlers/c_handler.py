from leet.lang_handlers.handler import LanguageHandler
from pathlib import Path
import os


class CHandler(LanguageHandler):
    @property
    def comment(self) -> str:
        return "// "
    
    @property
    def file_ext(self) -> str:
        return "c"
    
    def code_start(self, func_name: str) -> str:
        fmt_func_name = func_name.replace('-', '_').replace(' ', '_').lower()
        return """

#include <stdio.h>

void %s(int argc, char** argv) {
    // Implement here
    printf(\"Hello World!\\n\");   
}

int main(int argc, char** argv) {
    %s(argc, argv);
}

""" % (fmt_func_name, fmt_func_name)
    
    def run(self, file_path: Path):
        gcc_cmd = 'gcc'
        if os.name == 'nt':
            file_ext = '.exe'
        elif os.name == 'posix':
            file_ext = ''
        else:
            raise NotImplementedError(os.name)
        
        os.system(f"{gcc_cmd} {file_path} -o {file_path.name}{file_ext}")
        os.system(f"{file_path.name}{file_ext}")
    