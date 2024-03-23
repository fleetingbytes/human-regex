from abc import abstractmethod
from .abstract_regex import Abstract_Regex


class General_Regex_Base(Abstract_Regex):
    @classmethod
    @property
    @abstractmethod
    def JOINER(cls):
        ...

    @abstractmethod
    def join(self, *args, **kwargs):
        ...
