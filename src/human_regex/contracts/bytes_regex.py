from abc import abstractmethod
from .general_regex import General_Regex_Base


class Bytes_Regex_Base(bytes, General_Regex_Base):
    @classmethod
    @property
    def CONCATENATOR(cls):
        return b""
