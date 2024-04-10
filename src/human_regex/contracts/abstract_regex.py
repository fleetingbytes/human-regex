from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Self

Text_Element = str | bytes


class AbstractRegex(ABC):
    @classmethod
    @abstractmethod
    def concatenate(cls, args: Iterable[Text_Element]) -> Self: ...

    @abstractmethod
    def __add__(self, other: Text_Element) -> Self: ...

    @abstractmethod
    def __or__(self, other: Text_Element) -> Self: ...

    @abstractmethod
    def append(self, appendents: Iterable[Text_Element]) -> Self: ...

    @abstractmethod
    def prepend(self, prependents: Iterable[Text_Element]) -> Self: ...

    @abstractmethod
    def join(self, elements: Iterable[Text_Element]) -> Self: ...

    @property
    @abstractmethod
    def unnamed(self) -> Self: ...

    @property
    @abstractmethod
    def extension(self) -> Self: ...

    @classmethod
    @abstractmethod
    def set_flags(cls, flags: Text_Element) -> Self: ...

    @property
    @abstractmethod
    def no_capture(self) -> Self: ...

    @abstractmethod
    def modify_flags(self, flags: Text_Element) -> Self: ...

    @property
    @abstractmethod
    def atomic(self) -> Self: ...

    @abstractmethod
    def named(self, name) -> Self: ...

    @property
    @abstractmethod
    def backreference(self) -> Self: ...

    @property
    @abstractmethod
    def comment(self) -> Self: ...

    @abstractmethod
    def followed_by(self, following: Text_Element) -> Self: ...

    @abstractmethod
    def not_followed_by(self, not_following: Text_Element) -> Self: ...

    @abstractmethod
    def preceded_by(self, preceding: Text_Element) -> Self: ...

    @abstractmethod
    def not_preceded_by(self, not_preceding: Text_Element) -> Self: ...

    @classmethod
    @abstractmethod
    def yes_no(cls, id_name: int | Text_Element, yes: Text_Element, no: Text_Element | None = None) -> Self: ...

    @property
    @abstractmethod
    def set(self) -> Self: ...

    @property
    @abstractmethod
    def optional(self) -> Self: ...

    @property
    @abstractmethod
    def zero_or_more(self) -> Self: ...

    @property
    @abstractmethod
    def one_or_more(self) -> Self: ...

    @property
    @abstractmethod
    def lazy(self) -> Self: ...

    @abstractmethod
    def repeat(self, minimum, maximum=None, /) -> Self: ...

    @abstractmethod
    def exactly(self, number) -> Self: ...
