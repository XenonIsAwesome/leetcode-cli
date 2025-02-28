from pathlib import Path
import json


class ConfigUtils:
    default_settings = {
        "default_language": "python",
        "default_editor": "/usr/bin/env ed",
        "leet_path": "~/.leet/code/"
    }

    @staticmethod
    def get_config_path() -> Path:
        folder_path = Path.home() / ".leet"
        config_path = folder_path / "config.json"
        
        return config_path

    @staticmethod
    def get_config() -> dict:
        config_path = ConfigUtils.get_config_path()
        folder_path = config_path.parent
        
        folder_path.mkdir(exist_ok=True)
        if not config_path.exists():
            if config_path.is_dir():
                raise IsADirectoryError(config_path)
            config_path.write_text(json.dumps(ConfigUtils.default_settings))

        return json.loads(config_path.read_text())

    def __getitem__(self, name):
        return self.get_config().get(name) or \
            self.default_settings.get(name)
    
    def __setitem__(self, name, value):
        config: dict = self.get_config()
        config[name] = value
        
        config_path: Path = self.get_config_path()
        config_path.write_text(json.dumps(config))
        
