from abc import ABC, abstractmethod


class Abstract_Regex(ABC):
    @classmethod
    @property
    @abstractmethod
    def CONCATENATOR(cls):
        ...

    @abstractmethod
    def __add__(self):
        ...

    @abstractmethod
    def append(self):
        ...
