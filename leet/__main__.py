from argparse import ArgumentParser

from leet import ConfigUtils, ArgHandlerFactory, LangHandlerFactory


def parse_args():
    argparser = ArgumentParser(prog='leet')
    subparsers = argparser.add_subparsers(dest='command')
    
    # Get subcommand
    get_argparser = subparsers.add_parser("get")
    get_argparser.add_argument(
        "--lang", "--language", 
        default=ConfigUtils()["default_language"], 
        choices=LangHandlerFactory.keys(), 
        required=False
    )
    
    get_argparser.add_argument(
        "--editor", 
        default=ConfigUtils()["default_editor"], 
        required=False
    )
    
    get_argparser.add_argument(
        "--over", "--overwrite", 
        action='store_true',
        default=False,
        required=False
    )
    
    get_argparser.add_argument("question-slug-or-id", nargs='+')
    
    # Config subcommand
    config_argparser = subparsers.add_parser("config")
    config_argparser.add_argument(
        "setting", 
        choices=ConfigUtils.default_settings.keys()
    )
    config_argparser.add_argument("value")
    
    args = argparser.parse_args()
    ArgHandlerFactory.handle(args.command, args)


if __name__ == "__main__":
    parse_args()
