from abc import ABC, abstractmethod


class Abstract_Regex(ABC):
    @classmethod
    @property
    @abstractmethod
    def JOINER(cls):
        ...

    @abstractmethod
    def join(self):
        ...
