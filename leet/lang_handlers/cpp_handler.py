from leet.lang_handlers.handler import LanguageHandler
from pathlib import Path
import os


class CPPHandler(LanguageHandler):
    @property
    def comment(self) -> str:
        return "// "
    
    @property
    def file_ext(self) -> str:
        return "cpp"
    
    def code_start(self, func_name: str) -> str:
        fmt_func_name = func_name.replace('-', '_').replace(' ', '_').lower()
        return """

#include <iostream>

namespace Solution {
    void %s(int argc, char** argv) {
        // Implement here
        std::cout << \"Hello World!\" << std::endl;   
    }
}

int main(int argc, char** argv) {
    Solution::%s(argc, argv);
}

""" % (fmt_func_name, fmt_func_name)
    
    def run(self, file_path: Path):
        gcc_cmd = 'g++'
        if os.name == 'nt':
            file_ext = '.exe'
        elif os.name == 'posix':
            file_ext = ''
        else:
            raise NotImplementedError(os.name)
        
        os.system(f"{gcc_cmd} {file_path} -o {file_path.name}{file_ext}")
        os.system(f"{file_path.name}{file_ext}")
    