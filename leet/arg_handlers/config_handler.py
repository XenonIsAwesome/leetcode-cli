from leet import ConfigUtils

def config_handler(args):
    key = args.setting
    value = args.value
    
    if key == "default_editor":
        value = f"/usr/bin/env {value}"
    
    ConfigUtils()[key] = value