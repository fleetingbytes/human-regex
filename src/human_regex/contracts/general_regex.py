from abc import abstractmethod
from .abstract_regex import Abstract_Regex


class General_Regex_Base(Abstract_Regex):
    def append(self, *args, **kwargs):
        return type(self)(self.CONCATENATOR.join((self, *args), **kwargs))
