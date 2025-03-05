from pathlib import Path
import json


class ConfigUtils:
    default_settings = {
        "default_language": "python",
        "default_editor": "/usr/bin/env ed",
        "leet_path": str(Path.home() / ".leet")
    }

    @property
    def config_path(self) -> Path:
        folder_path = Path.home() / ".leet"
        config_path = folder_path / "config.json"
        
        return config_path

    @property
    def config(self) -> dict:
        config_path = self.config_path
        folder_path = config_path.parent
        
        folder_path.mkdir(exist_ok=True)
        if not config_path.exists():
            if config_path.is_dir():
                raise IsADirectoryError(config_path)
            config_path.write_text(json.dumps(ConfigUtils.default_settings))

        return json.loads(config_path.read_text())

    def __getitem__(self, name):
        value = self.get(name)
        if value is None:
            raise KeyError(name)
        return value
    
    def __setitem__(self, name, value):
        config = self.config
        config[name] = value        
        self.config_path.write_text(json.dumps(config))
        
    def get(self, name):
        return self.config.get(name) or \
            self.default_settings.get(name)
        
