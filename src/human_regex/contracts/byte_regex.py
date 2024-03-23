from abc import abstractmethod
from .general_regex import General_Regex_Base


class Byte_Regex_Base(bytes, General_Regex_Base):
    @classmethod
    @property
    def JOINER(cls):
        return b""

    @abstractmethod
    def join(self):
        ...
