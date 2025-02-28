from abc import ABC, abstractmethod
from pathlib import Path

class LanguageHandler(ABC):
    @property
    @abstractmethod
    def comment() -> str:
        raise NotImplementedError
    
    @property
    @abstractmethod
    def file_ext() -> str:
        raise NotImplementedError
    
    @abstractmethod
    def code_start(func_name: str):
        raise NotImplementedError

    @abstractmethod
    def run(file_path: Path):
        raise NotImplementedError
