from argparse import ArgumentParser
import json
from leet import ConfigUtils




def config_handler(args):
    key = args.setting
    value = args.value
    
    if key == "default_editor":
        value = f"/usr/bin/env {value}"
    
    ConfigUtils()[key] = value
    
    
leet_handlers = {
    'get': get_handler,
    'config': config_handler
}

if __name__ == "__main__":
    argparser = ArgumentParser(prog='leet')
    subparsers = argparser.add_subparsers(dest='command')
    
    get_argparser = subparsers.add_parser("get")
    get_argparser.add_argument("--lang", "--language", default=get_config_value("default_language"), choices=language_handlers.keys(), required=False)
    get_argparser.add_argument("--editor", default=get_config_value("default_editor"), required=False)
    get_argparser.add_argument("question-slug-or-id")
    
    config_argparser = subparsers.add_parser("config")
    config_argparser.add_argument("setting", choices=default_settings.keys())
    config_argparser.add_argument("value")
    
    args = argparser.parse_args()
    leet_handlers[args.command](args)
    