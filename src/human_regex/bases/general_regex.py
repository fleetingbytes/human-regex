from abc import abstractmethod
from collections.abc import Iterable
from typing import Self
import json
from requests import request
import re

from ..contracts.abstract_regex import AbstractRegex

Text_Element = str | bytes


class GeneralRegexBase(AbstractRegex):
    @classmethod
    @property
    @abstractmethod
    def EMPTY(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def OPEN_CHAR_SET(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def CLOSE_CHAR_SET(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def OPEN_GROUP(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def CLOSE_GROUP(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def OPEN_EXTENSION(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def CLOSE_EXTENSION(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def OPEN_NAME(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def CLOSE_NAME(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def OPEN_QUANTIFIER(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def CLOSE_QUANTIFIER(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def QUANTIFIER_SEPARATOR(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def OR(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def NO_CAPTURE(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def FLAGS_END(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def ATOMIC(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def NAME_REFERENCE(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def COMMENT(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def FOLLOWED_BY(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def NOT_FOLLOWED_BY(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def PRECEDED_BY(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def NOT_PRECEDED_BY(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def ZERO_OR_MORE(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def ONE_OR_MORE(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def OPTIONAL(cls) -> Text_Element:
        ...

    @classmethod
    @property
    @abstractmethod
    def LAZY(cls) -> Text_Element:
        ...

    @classmethod
    def concatenate(cls, args: Iterable[Text_Element]) -> Self:
        str_or_bytes = str if str in cls.__mro__ else bytes
        result = str_or_bytes(cls.EMPTY).join(args)
        return cls(result)

    def __add__(self, other: Text_Element) -> Self:
        cls = type(self)
        return cls.concatenate((self, other))

    def __or__(self, other) -> Self:
        cls = type(self)
        return cls.concatenate((self, cls.OR, other))

    def append(self, appendent: Text_Element) -> Self:
        cls = type(self)
        return cls.concatenate((self, appendent))

    def prepend(self, prependent: Text_Element) -> Self:
        cls = type(self)
        return cls.concatenate((prependent, self))

    def join(self, elements: Iterable[Text_Element]) -> Self:
        cls = type(self)
        str_or_bytes = str if str in cls.__mro__ else bytes
        result = str_or_bytes(self).join(elements)
        return cls(result)

    @property
    def unnamed(self) -> Self:
        cls = type(self)
        return cls.concatenate((cls.OPEN_GROUP, self, cls.CLOSE_GROUP))

    @property
    def extension(self) -> Self:
        cls = type(self)
        return cls.concatenate((cls.OPEN_EXTENSION, self, cls.CLOSE_EXTENSION))

    @classmethod
    def set_flags(cls, flags: Text_Element) -> Self:
        return cls(flags).extension

    @property
    def no_capture(self) -> Self:
        cls = type(self)
        return cls.concatenate((cls.NO_CAPTURE, self)).extension

    def modify_flags(self, flags: Text_Element) -> Self:
        cls = type(self)
        return cls.concatenate((self, cls(flags).extension))

    @property
    def atomic(self) -> Self:
        cls = type(self)
        return cls.concatenate((cls.ATOMIC, self)).extension

    def named(self, name: Text_Element) -> Self:
        cls = type(self)
        label = cls.concatenate((cls.OPEN_NAME, name, cls.CLOSE_NAME))
        return cls.concatenate((label, self)).extension

    @property
    def backreference(self) -> Self:
        cls = type(self)
        return cls.concatenate((cls.NAME_REFERENCE, self)).extension

    @property
    def comment(self) -> Self:
        cls = type(self)
        return cls.concatenate((cls.COMMENT, self)).extension

    def followed_by(self, following: Text_Element) -> Self:
        cls = type(self)
        follows = cls.concatenate((cls.FOLLOWED_BY, following)).extension
        return cls.concatenate((self, follows))

    def not_followed_by(self, not_following: Text_Element) -> Self:
        cls = type(self)
        does_not_follow = cls.concatenate((cls.NOT_FOLLOWED_BY, not_following)).extension
        return cls.concatenate((self, does_not_follow))

    def preceded_by(self, preceding: Text_Element) -> Self:
        cls = type(self)
        precedes = cls.concatenate((cls.PRECEDED_BY, preceding)).extension
        return cls.concatenate((precedes, self))

    def not_preceded_by(self, not_preceding: Text_Element) -> Self:
        cls = type(self)
        does_not_precede = cls.concatenate((cls.NOT_PRECEDED_BY, not_preceding)).extension
        return cls.concatenate((does_not_precede, self))

    @classmethod
    def yes_no(cls, id_name: int | Text_Element, yes: Text_Element, no: Text_Element | None = None) -> Self:
        id_name = cls._convert_to_bytes_or_string(id_name) if isinstance(id_name, int) else id_name
        result = cls.concatenate((cls(id_name).unnamed, yes))
        if no is not None:
            result += cls.concatenate((cls.OR, no))
        return result.extension

    @classmethod
    def _convert_to_bytes_or_string(cls, i: int) -> Text_Element:
        i = str(i)
        if bytes in cls.__mro__:
            i = i.encode()
        return i

    @property
    def set(self) -> Self:
        cls = type(self)
        return cls.concatenate((cls.OPEN_CHAR_SET, self, cls.CLOSE_CHAR_SET))

    @property
    def optional(self) -> Self:
        cls = type(self)
        return cls.concatenate((self, cls.OPTIONAL))

    @property
    def zero_or_more(self) -> Self:
        cls = type(self)
        return cls.concatenate((self, cls.ZERO_OR_MORE))

    @property
    def one_or_more(self) -> Self:
        cls = type(self)
        return cls.concatenate((self, cls.ONE_OR_MORE))

    @property
    def lazy(self) -> Self:
        cls = type(self)
        return cls.concatenate((self, cls.LAZY))

    def repeat(self, minimum, maximum=None, /) -> Self:
        cls = type(self)
        minimum = cls._convert_to_bytes_or_string(minimum) if minimum is not None else cls.EMPTY
        maximum = cls._convert_to_bytes_or_string(maximum) if maximum is not None else cls.EMPTY
        return cls.concatenate(
            (self, cls.OPEN_QUANTIFIER, minimum, cls.QUANTIFIER_SEPARATOR, maximum, cls.CLOSE_QUANTIFIER)
        )
