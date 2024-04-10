## Overview

Regular expressions for humans.

Human-regex provides the classes `StringRegex` and `BytesRegex` which are subclasses of `str` or `bytes`, respectively. They contain methods and properties which can produce your regular expressions with *readable code*.

```py
from human_regex import StringRegex as Sre

regex = Sre("match")
assert regex == "match"

regex = regex.not_preceded_by("element")
assert regex == "(?<!element)match"

regex = regex.named("my_group")
assert regex == "(?P<my_group>(?<!element)match)"

regex = Sre("match").not_preceded_by("element").named("my_group").optional
assert regex == "(?P<my_group>(?<!element)match)?"
```

Let's construct regular expressions for words ending in with the letter "c"
and also for words starting with the letter "a":

```py
from human_regex import StringRegex as Sre

word = Sre(r"\w").zero_or_more
assert word == r"\w*"

word_endswith_c = word.append("c").named("ends_with_c").prepend(r"\b").append(r"\b")
assert word_endswith_c == r"\b(?P<ends_with_c>\w*c)\b"

word_startswith_a = word.prepend("a").named("starts_with_a").prepend(r"\b").append(r"\b")
assert word_startswith_a == r"\b(?P<starts_with_a>a\w*)\b"
```

## Subclasses of `str`, `bytes`

`StringRegex` and `BytesRegex` are subclasses of `str` or `bytes`, respectively. They interoperate with these objects seamlessly. Here are some alternative ways how to construct the pattern from the previous example in the Overview section. Here we mix `StringRegex` and `str` instances:

```py
from human_regex import StringRegex as Sre

word = Sre(r"\w")
word += "*"
assert word == r"\w*"
assert isinstance(word, Sre)
assert isinstance(word, str)

word_endswith_c: str = "".join((r"\b", "(?P<ends_with_c>", word, "c", ")", r"\b"))
word_endswith_c: Sre = Sre(word_endswith_c)
# same as:
word_endswith_c: Sre = Sre("").join((r"\b", "(?P<ends_with_c>", word, "c", ")", r"\b"))
word_endswith_c: Sre = Sre.concatenate((r"\b", "(?P<ends_with_c>", word, "c", ")", r"\b"))
```

## Proxy `re` Module's Functions and Flags

`StringRegex` and `BytesRegex` objects proxy the class `re.RegexFlag` and all flags and functions of the built-in `re` module (i.e. `re.compile`, `re.search`, etc.). These fuctions automatically take the `StringRegex` or `BytesRegex` instance object as their first argument:

```py
from human_regex import StringRegex as Sre
import re  # needed only for the assert statements below

assert Sre.RegexFlag is re.RegexFlag

sre = Sre("abc.")
# Use the proxied `re.compile` function of the StringRegex instance
# and the proxied flags on the StringRegex class
compiled = sre.compile(flags=Sre.IGNORECASE | Sre.DOTALL)
# same as:
# compiled = re.compile(sre, flags=re.IGNORECASE | re.DOTALL)
assert isinstance(compiled, re.Pattern)

text = "abc\nABCd\n\Abc"

found = sre.findall(text, flags=Sre.IGNORECASE | Sre.DOTALL)
# same as:
# found = re.findall(sre, text, flags=re.IGNORECASE | re.DOTALL)
assert found == ["abc\n", "ABCd"]
```

## StringRegex and BytesRegex

Every method demonstated with `StringRegex` is available on `BytesRegex` and is applicable to `bytes` objects, rather than `str` objects:

```py
from human_regex import StringRegex as Sre, BytesRegex as Bre
import re  # needed only for the assert statements below

string_re = Sre("abc.").named("my_group")
string_pattern = string_re.compile(flags=Sre.IGNORECASE | Sre.DOTALL)
assert isinstance(string_pattern, re.Pattern)

bytes_re = Bre(b"abc.").named(b"my_group")
bytes_pattern = bytes_re.compile(flags=Bre.IGNORECASE | Bre.DOTALL)
assert isinstance(bytes_pattern, re.Pattern)

assert string_pattern.flags == 50 # includes the implicit Sre.UNICODE flag
assert bytes_pattern.flags == 18 # bytes patterns cannot use the UNICODE flag
assert (Bre.IGNORECASE | Bre.DOTALL | Bre.UNICODE).value == 50
```

## Caution When Iterating Over Bytes Objects

Iterating over `str` instances will yield individual string characters, but iterating over `bytes` instances will yield instances of `int`.

```py
some_strings = "abc"
assert tuple(some_strings) == ("a", "b", "c")
s: str = "".join(some_strings) # iterates over "abc" and joins its elements
assert s == "abc"

some_integers = b"abc"
assert tuple(some_integers) == (97, 98, 99)
b: bytes = b"".join(some_integers)
# will raise a TypeError because elements of the iterable b"abc"
# are the integers 97, 98, 99 but bytes.join
# expects instances of bytes-like objects
```

`StringRegex` and `BytesRegex` are subclasses of `str` and `bytes` respectively, so they inherit this behavior. You can use a `StringRegex` instance as an iterable of string characters, but iterating over a `BytesRegex` instance will yield integers. Methods `BytesRegex.concatenate` and `BytesRegex.join`, both of which use `bytes.join` internally, cannot work with iterables of integers. They expect iterables of bytes-like objects.

```py
from human_regex import BytesRegex as Bre

# as long as the iterable yields bytes-like objects, everyting is fine:
some_bytes = (b"a", Bre(b"b"), b"c")
assert Bre.concatenate(some_bytes) == Bre(b"abc")

some_integers = Bre(b"abc")
b = Bre.concatenate(some_integers) # will raise a TypeError
# because the elements of Bre(b"abc") are integers,
# rather than bytes-like objects:
assert tuple(Bre(b"abc")) == (97, 98, 99)

# we would have to convert the integers to string characters and encode them to bytes:
b = Bre.concatenate(map(lambda i: str.encode(chr(i)), some_integers))
```

## Inherited Methods and Properties

`StringRegex` and `BytesRegex` differ slightly in their private class variables, but their public methods and properties have all been inherited from the `human_regex.bases.general_regex.GeneralRegexBase` class. Thus, the documentation of the `StringRegex` or `BytesRegex`'s inherited public methods and properties is to be looked up there. For methods proxied from the built-in [re](https://docs.python.org/library/re.html) module or inherited from `str`, or `bytes`, look in the Python's standard library documentation.

## Links

- [Repository](https://github.com/fleetingbytes/human-regex)
- [Documentation](https://fleetingbytes.github.io/human-regex/human_regex.html)

