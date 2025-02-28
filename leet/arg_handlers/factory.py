from typing import Any, Dict, Callable

from leet.arg_handlers import config_handler, get_handler

ArgParserCommand = str
ArgHandler = Callable[[Any], None]


class ArgHandlerFactory:
    arg_handlers: Dict[ArgParserCommand, ArgHandler] = {
        "config": config_handler,
        "get": get_handler,
    }
    
    @staticmethod
    def handle(command, args):
        if command not in ArgHandlerFactory.arg_handlers:
            raise KeyError(command)
        
        handler: ArgHandler = ArgHandlerFactory.arg_handlers[command]
        handler(args)
