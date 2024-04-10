"""
All examples here are written for the `human_regex.StringRegex` variant, but
they are equally applicable for the `human_regex.BytesRegex` variant, if you
use byte-strings (`b"..."`) instead of strings (`"..."`).
"""

from abc import abstractmethod
from collections.abc import Iterable
from typing import Self

from ..contracts.abstract_regex import AbstractRegex

Text_Element = str | bytes
"""
@private
"""


class GeneralRegexBase(AbstractRegex):
    """
    Base class for `human_regex.StringRegex` and `human_regex.BytesRegex`.
    """

    @classmethod
    @property
    @abstractmethod
    def EMPTY(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def OPEN_CHAR_SET(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def CLOSE_CHAR_SET(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def OPEN_GROUP(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def CLOSE_GROUP(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def OPEN_EXTENSION(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def CLOSE_EXTENSION(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def OPEN_NAME(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def CLOSE_NAME(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def OPEN_QUANTIFIER(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def CLOSE_QUANTIFIER(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def QUANTIFIER_SEPARATOR(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def OR(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def NO_CAPTURE(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def FLAGS_END(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def ATOMIC(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def NAME_REFERENCE(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def COMMENT(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def FOLLOWED_BY(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def NOT_FOLLOWED_BY(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def PRECEDED_BY(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def NOT_PRECEDED_BY(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def ZERO_OR_MORE(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def ONE_OR_MORE(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def OPTIONAL(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    @property
    @abstractmethod
    def LAZY(cls) -> Text_Element:
        """
        @private
        """
        ...

    @classmethod
    def concatenate(cls, elements: Iterable[Text_Element]) -> Self:
        """
        Concatenates items in *elements*. Returns `StringRegex` instance of the joined string.

        ```py
        from human_regex import StringRegex as Sre

        sre = Sre.concatenate(("Hello", " ", "world"))
        assert sre == Sre("Hello world")
        # equivalent to the following:
        sre = Sre("".join(("Hello", " ", "world")))
        sre = Sre("").join(("Hello", " ", "world"))
        sre = Sre("Hello") + " " + "world"
        ```
        """
        str_or_bytes = str if str in cls.__mro__ else bytes
        result = str_or_bytes(cls.EMPTY).join(elements)
        return cls(result)

    def __add__(self, other: Text_Element) -> Self:
        """
        @public
        Support of the `+` operator. Returns a new `StringRegex` instance which has *other*
        appended to the original `StringRegex` instance.

        ```py
        from human_regex import StringRegex as Sre

        sre1 = Sre("abc")
        sre2 = Sre("def")
        sre = sre1 + sre2
        assert sre == Sre("abcdef")

        # identical to:
        sre = Sre("abc") + "def"
        ```
        """
        cls = type(self)
        return cls.concatenate((self, other))

    def __or__(self, other) -> Self:
        """
        @public
        Support of the `|` operator. Returns a new `StringRegex` instance which is
        the original instance joined with *other* using the `|` symbol.

        ```py
        from human_regex import StringRegex as Sre

        sre1 = Sre("abc")
        sre2 = Sre("def")
        sre = sre1 | sre2
        assert sre == Sre("abc|def")

        # identical to:
        sre = Sre("abc") | "def"
        ```
        """
        cls = type(self)
        return cls.concatenate((self, cls.OR, other))

    def append(self, appendent: Text_Element) -> Self:
        """
        @public
        Returns a new `StringRegex` instance which is the original instance
        followed by *appendent*.

        ```py
        from human_regex import StringRegex as Sre

        sre = Sre("pretty").append(" little").append(Sre(" angel"))
        assert sre == Sre("pretty little angel")
        ```
        """
        cls = type(self)
        return cls.concatenate((self, appendent))

    def prepend(self, prependent: Text_Element) -> Self:
        """
        @public
        Returns a new `StringRegex` instance with *self*
        following the *prependent*.

        This is useful when an already defined `StringRegex` instance is used
        as a building block of a more complex `StringRegex` and we need
        to add some `str` instances before it.

        ```py
        from human_regex import StringRegex as Sre

        party = Sre("Party")
        # Intention: to add the strings "A Long-" and "Expected "
        # before the `party` instance.
        #
        # The built-in str does not have an .append method, so this will fail:
        # "A Long-".append("Expected" ").append(party).
        #
        # If we use string addition, we would get a str instance
        # rather than a StringRegex instance:
        # s: str = "A Long-" + "Expected " + party
        #
        # To get a StringRegex instance, we can turn things around
        # and instead prepend normal str instances to a StringRegex:
        sre: Sre = party.prepend("Expected ").prepend("A Long-")
        assert sre == Sre("A Long-Expected Party")

        # Alternative: convert the starting element to StringRegex and add the rest:
        sre: Sre = Sre("A Long-") + "Expected" + party
        # Or concatenate:
        sre: Sre = Sre.concatenate(("A Long-", "Expected ", party))
        ```
        """
        cls = type(self)
        return cls.concatenate((prependent, self))

    def join(self, elements: Iterable[Text_Element]) -> Self:
        # ruff: noqa: RUF002, E501
        """
        @public
        Analogous to `str.join`, but produces instances of `StringRegex`:

        ```py
        from human_regex import StringRegex as Sre

        sre = Sre(" ").join(("hello", "world"))
        assert sre == Sre("hello world")
        ```

        A more complex example: A suboptimal regular expression for
        parsing geographical longitude in the form *127° 36′ 52″ W*:

        ```py
        from human_regex import StringRegex as Sre

        coordinates = Sre(" ").join((
            Sre(r"\\d").repeat(1, 3).named("degrees").append("°"),
            Sre(r"\\d").repeat(1, 2).named("minutes").append("′"),
            Sre(r"\\d").repeat(1, 2).named("seconds").append("″"),
            Sre("EW").set.named("direction"),
        )).named("coordinates")
        assert coordinates == r"(?P<coordinates>(?P<degrees>\\d{1,3})° (?P<minutes>\\d{1,2})′ (?P<seconds>\\d{1,2})″ (?P<direction>[EW]))"
        ```
        (The resulting regular expression is suboptimal because it would capture values of degrees, minutes, seconds which
        are illegal or not part of the longitude notation norm, e.g. `190° 78′ 93″ E` would be a match.)
        """
        cls = type(self)
        str_or_bytes = str if str in cls.__mro__ else bytes
        result = str_or_bytes(self).join(elements)
        return cls(result)

    @property
    def unnamed(self) -> Self:
        """
        @public
        Creates an unnamed group with the contents of *self*.

        ```py
        from human_regex import StringRegex as Sre

        number = Sre(r"\\d").one_or_more.unnamed
        assert number == "(\\d+)"
        sre = number.prepend("My favorite number is ").append(r"\\.")
        assert sre == "My favorite number is (\\d+)\\."
        ```
        """
        cls = type(self)
        return cls.concatenate((cls.OPEN_GROUP, self, cls.CLOSE_GROUP))

    @property
    def extension(self) -> Self:
        """
        @public
        Returns a new `StringRegex` instance with *self* inside the extension notation `(?...)`:

        ```py
        from human_regex import StringRegex as Sre

        sre: Sre = Sre("something").extension
        assert sre == "(?something)"
        ```
        """
        cls = type(self)
        return cls.concatenate((cls.OPEN_EXTENSION, self, cls.CLOSE_EXTENSION))

    @classmethod
    def set_flags(cls, flags: Text_Element) -> Self:
        """
        @public
        A way of encoding regular expression flags into the expression string itself,
        rather than passing it as *flag* argument to the `StringRegex.compile` or other methods.
        This should only be used at the start of a regular expression.

        Returns a `StringRegex` instance which sets the given *flags*. Flags can be one
        or more letters from the set `a`, `i`, `L`, `m`, `s`, `u`, `x`.
        Refer to the documentation of [re](https://docs.python.org/library/re.html),
        search there for "aiLmsux".

        ```py
        from human_regex import StringRegex as Sre

        # Create an expression with Sre.MULTILINE | Sre.IGNORECASE
        sre = Sre.set_flags("mi").append("match.this")
        assert sre == "(?mi)match.this"
        ```
        """
        return cls(flags).extension

    @property
    def no_capture(self) -> Self:
        """
        @public
        Returns a new `StringRegex` with a non-capturing group made of *self*:

        ```py
        from human_regex import StringRegex as Sre

        sre = Sre("match").no_capture
        assert sre == "(?:match)"
        ```
        """
        cls = type(self)
        return cls.concatenate((cls.NO_CAPTURE, self)).extension

    def modify_flags(self, flags: Text_Element) -> Self:
        """
        @public
        Allows you to set different flags for a part of a more complex expression.

        Returns a new `StringRegex` instance with *self* inside the
        modify-flags-extension with flags modified as specified by the
        *flags* argument. Flags can be one
        or more letters from the set `a`, `i`, `L`, `m`, `s`, `u`, `x`, optionally
        followed by "-" followed by one or more letters from the `i`, `m`, `s`, `x` set.


        Refer to the documentation of [re](https://docs.python.org/library/re.html),
        search there for "aiLmsux-imsx".

        ```py
        from human_regex import StringRegex as Sre
        part1 = Sre.set_flags("mi").append("multiline.and.ignore.case.here")
        assert part1 == "(?mi)multiline.and.ignore.case.here"
        part2 = Sre("add.dot.all.but.do.NOT.ignore.case.HERE.and.no.multiline").modify_flags("s-im")
        assert part2 == "(?s-im:add.dot.all.but.do.NOT.ignore.case.HERE.and.no.multiline)"
        part3 = "again.multiline.and.ignore.case.here"
        sre = Sre.concatenate((part1, part2, part3))
        assert sre == "(?mi)multiline.and.ignore.case.here(?s-im:add.dot.all.but.do.NOT.ignore.case.HERE.and.no.multiline)again.multiline.and.ignore.case.here"
        ```
        """
        cls = type(self)
        extension_core = cls.concatenate((flags, cls.FLAGS_END, self))
        return extension_core.extension

    @property
    def atomic(self) -> Self:
        """
        @public
        Returns a new `StringRegex` instance with *self* as the content of an *atomic group*.

        ```py
        from human_regex import StringRegex as Sre

        sre = Sre("content").atomic
        assert sre == "(?>content)"
        ```
        """
        cls = type(self)
        return cls.concatenate((cls.ATOMIC, self)).extension

    def named(self, name: Text_Element) -> Self:
        """
        @public
        Returns a new `StringRegex` instance with *self* as the content of a group named *name*.

        ```py
        from human_regex import StringRegex as Sre

        word = Sre(r"\\w").one_or_more # \\w+
        burger = word.named("burger")
        assert burger == r"(?P<burger>\\w+)"
        extra = word.named("extra")
        assert extra == r"(?P<extra>\\w+)"

        sre = burger + " with " + extra
        assert sre == r"(?P<burger>\\w+) with (?P<extra>\\w+)"

        match = sre.match("quarterpounder with cheese")
        assert match.group("burger") == "quarterpounder"
        assert match.group("extra") == "cheese"
        ```
        """
        cls = type(self)
        label = cls.concatenate((cls.OPEN_NAME, name, cls.CLOSE_NAME))
        return cls.concatenate((label, self)).extension

    @property
    def backreference(self) -> Self:
        """
        @public
        Returns `StringRegex` instance with *self* as the name of the group being refered back to.

        ```py
        from human_regex import StringRegex as Sre

        word = Sre(r"\\w").one_or_more # \\w+
        old_ruler = word.named("ruler") # (?P<ruler>\\w+)
        new_ruler = Sre("ruler").backreference # (?P=ruler)
        sre = Sre(" ").join(("The", old_ruler, "is dead, long live the", new_ruler.append("!")))

        assert sre == "The (?P<ruler>\\w+) is dead, long live the (?P=ruler)!"
        text = "The king is dead, long live the king!"
        assert sre.match(text)
        ```
        """
        cls = type(self)
        return cls.concatenate((cls.NAME_REFERENCE, self)).extension

    @property
    def comment(self) -> Self:
        """
        @public
        Returns a new `StringRegex` with *self* as a comment.

        ```py
        from human_regex import StringRegex as Sre

        sre = Sre(r"0-9a-f").set + Sre("any hex digit").comment
        assert sre == "[0-9a-f](?#any hex digit)"
        ```
        """
        cls = type(self)
        return cls.concatenate((cls.COMMENT, self)).extension

    def followed_by(self, following: Text_Element) -> Self:
        """
        @public
        Returns a new `StringRegex` with *self* extended by *following* as the *positive lookahead assertion*.

        ```py
        from human_regex import StringRegex as Sre

        sre = Sre("Isaac ").followed_by("Asimov")
        assert sre == "Isaac (?=Asimov)"
        ```
        """
        cls = type(self)
        follows = cls.concatenate((cls.FOLLOWED_BY, following)).extension
        return cls.concatenate((self, follows))

    def not_followed_by(self, not_following: Text_Element) -> Self:
        """
        @public
        Returns a new `StringRegex` with *self* extended by *not_following* as the *negative lookahead assertion*.

        ```py
        from human_regex import StringRegex as Sre

        sre = Sre("Isaac ").not_followed_by("Asimov")
        assert sre == "Isaac (?!Asimov)"
        ```
        """
        cls = type(self)
        does_not_follow = cls.concatenate((cls.NOT_FOLLOWED_BY, not_following)).extension
        return cls.concatenate((self, does_not_follow))

    def preceded_by(self, preceding: Text_Element) -> Self:
        """
        @public
        Returns a new `StringRegex` with *self* extended by *preceding* as the *positive lookbehind assertion*.

        ```py
        from human_regex import StringRegex as Sre

        sre = Sre("chat").preceded_by("chit")
        assert sre == "(?<=chit)chat"
        ```
        """
        cls = type(self)
        precedes = cls.concatenate((cls.PRECEDED_BY, preceding)).extension
        return cls.concatenate((precedes, self))

    def not_preceded_by(self, not_preceding: Text_Element) -> Self:
        """
        @public
        Returns a new `StringRegex` with *self* extended by *not_preceding* as the *negative lookbehind assertion*.

        ```py
        from human_regex import StringRegex as Sre

        sre = Sre("chat").not_preceded_by("chit")
        assert sre == "(?<!chit)chat"
        ```
        """
        cls = type(self)
        does_not_precede = cls.concatenate((cls.NOT_PRECEDED_BY, not_preceding)).extension
        return cls.concatenate((does_not_precede, self))

    @classmethod
    def yes_no(cls, id_name: int | Text_Element, yes: Text_Element, no: Text_Element | None = None) -> Self:
        """
        @public
        Constructs the *yes-no-pattern* which will match with *yes*-pattern
        if the group with given *id_name* exists, and with *no*-pattern if it doesn't.
        *no*-pattern is optional and can be omitted. *id_name* can be the number
        of the group or the name of the group if the group was named.

        Example: Recreating the expression `(<)?(\\w+@\\w+(?:\\.\\w+)+)(?(1)>|$)`
        from the built-in documentation of [re](https://docs.python.org/library/re.html)
        for a poor email matching pattern, which will match with `<user@host.com>` as well as
        `user@host.com`, but not with `<user@host.com` nor `user@host.com>`:

        ```py
        from human_regex import StringRegex as Sre

        word = Sre(r"\\w").one_or_more # \\w+
        mail_core = (
            word +
            "@" +
            word +
            word.prepend(r"\\.").no_capture.one_or_more
        ).unnamed # (\\w+@\\w+(?:\\.\\w+)+)
        maybe_less_than = Sre("<").unnamed.optional # (<)?
        maybe_greater_than = Sre.yes_no(1, ">", "$") # (?(1)>|$)
        mail_re = maybe_less_than + mail_core + maybe_greater_than

        assert mail_re == r"(<)?(\\w+@\\w+(?:\\.\\w+)+)(?(1)>|$)"
        ```
        """
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
        """
        @public
        Returns a new `StringRegex` for a set of *self*.

        ```py
        from human_regex import StringRegex as Sre

        hex_digits = Sre("a-f0-9").set
        assert hex_digits == "[a-f0-9]"
        ```
        """
        cls = type(self)
        return cls.concatenate((cls.OPEN_CHAR_SET, self, cls.CLOSE_CHAR_SET))

    @property
    def optional(self) -> Self:
        """
        @public
        Returns a new `StringRegex` with `?` appended to *self*.

        ```py
        from human_regex import StringRegex as Sre

        character = Sre(r"\\w")
        optional_character = character.optional
        assert optional_character == r"\\w?"
        ```
        """
        cls = type(self)
        return cls.concatenate((self, cls.OPTIONAL))

    @property
    def zero_or_more(self) -> Self:
        """
        @public
        Returns a new `StringRegex` with `*` appended to *self*.

        ```py
        from human_regex import StringRegex as Sre

        digit = Sre(r"\\d")
        maybe_digits = digit.zero_or_more
        assert maybe_digits == r"\\d*"
        ```
        """
        cls = type(self)
        return cls.concatenate((self, cls.ZERO_OR_MORE))

    @property
    def one_or_more(self) -> Self:
        """
        @public
        Returns a new `StringRegex` with `+` appended to *self*.

        ```py
        from human_regex import StringRegex as Sre

        digit = Sre(r"\\d")
        some_digits = digit.one_or_more
        assert some_digits == r"\\d+"
        ```
        """
        cls = type(self)
        return cls.concatenate((self, cls.ONE_OR_MORE))

    @property
    def lazy(self) -> Self:
        """
        @public
        Returns a new `StringRegex` with `?` appended to *self*.

        ```py
        from human_regex import StringRegex as Sre

        everything = Sre(".*")
        assert everything.lazy == ".*?"

        tab = Sre(r"\\t")
        everything_before_first_tab = everything.prepend("^").lazy.named("before_tab").append(tab)
        assert everything_before_first_tab == r"(?P<before_tab>^.*?)\\t"
        ```
        """
        cls = type(self)
        return cls.concatenate((self, cls.LAZY))

    def repeat(self, minimum, maximum, /) -> Self:
        """
        @public
        Returns a new `StringRegex` with a greedy quantifier appended to *self*.
        *minimum* and *maximum* specify limits of repetition. *maximum* is optional

        ```py
        from human_regex import StringRegex as Sre

        two_or_more_As = Sre("A").repeat(2, None)
        assert two_or_more_As == "A{2,}"
        two_to_four_As = Sre("A").repeat(2, 4)
        assert two_to_four_As == "A{2,4}"
        up_to_four_As = Sre("A").repeat(None, 4)
        assert up_to_four_As == "A{,4}"
        ```
        """
        cls = type(self)
        minimum = cls._convert_to_bytes_or_string(minimum) if minimum is not None else cls.EMPTY
        maximum = cls._convert_to_bytes_or_string(maximum) if maximum is not None else cls.EMPTY
        return cls.concatenate(
            (self, cls.OPEN_QUANTIFIER, minimum, cls.QUANTIFIER_SEPARATOR, maximum, cls.CLOSE_QUANTIFIER)
        )

    def exactly(self, number: int) -> Self:
        """
        @public
        Returns a new `StringRegex` with a fixed quantifier of *number* appended to *self*.

        ```py
        from human_regex import StringRegex as Sre

        three_As = Sre("A").exactly(3)
        assert three_As == "A{3}"
        ```
        """
        cls = type(self)
        number = cls._convert_to_bytes_or_string(number) if number else cls.EMPTY
        return cls.concatenate((self, cls.OPEN_QUANTIFIER, number, cls.CLOSE_QUANTIFIER))
