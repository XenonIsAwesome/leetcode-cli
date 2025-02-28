from leet.lang_handlers import PythonHandler, CHandler, CPPHandler, LanguageHandler

class LangHandlerFactory:
    lang_handlers = {
        ["py", "python", "python3"]: PythonHandler(),
        ["c"]: CHandler(),
        ["cpp", "c++", "cplusplus"]: CPPHandler()
    }
    
    @staticmethod
    def get(key: str) -> LanguageHandler:
        for keys, handler in LangHandlerFactory.lang_handlers.items():
            if key in keys:
                return handler