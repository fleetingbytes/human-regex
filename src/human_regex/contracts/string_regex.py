from abc import abstractmethod
from .general_regex import General_Regex_Base


class String_Regex_Base(str, General_Regex_Base):
    @classmethod
    @property
    def CONCATENATOR(cls):
        return ""
