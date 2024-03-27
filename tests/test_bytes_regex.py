from human_regex import BytesRegex as Bre
import re


def test_bytes_concatenate():
    b = Bre.concatenate((b"a", b"b", b"c"))
    assert b == b"abc"
    assert type(b) is Bre


def test_bytes_add():
    b = Bre(b"this") + b" " + b"and" + b" " + b"that"
    assert b == b"this and that"
    assert type(b) is Bre
    b = Bre(b"this") + Bre(b" ") + Bre(b"and") + Bre(b" ") + Bre(b"that")
    assert b == b"this and that"
    assert type(b) is Bre


def test_bytes_or():
    b = Bre(b"cyan") | b"magenta" | b"yellow" | b"black"
    assert b == b"cyan|magenta|yellow|black"
    assert type(b) is Bre


def test_bytes_append():
    b = Bre(b"hi")
    c = b.append(b" ").append(b"there")
    assert c == b"hi there"
    assert type(c) is Bre


def test_bytes_prepend():
    b = Bre(b"Party").prepend(b"Expected ").prepend(b"Long-").prepend(b"A ")
    assert b == b"A Long-Expected Party"
    assert type(b) is Bre


def test_bytes_join():
    b = Bre(b", ").join((b"apples", b"pears", b"oranges"))
    assert b == b"apples, pears, oranges"
    assert type(b) is Bre


def test_bytes_unnamed():
    b = Bre(b"content").unnamed
    assert b == b"(content)"
    assert type(b) is Bre


def test_bytes_set_flags():
    b = Bre.set_flags(b"aiLmsux")
    assert b == b"(?aiLmsux)"
    assert type(b) is Bre


def test_bytes_no_capture():
    b = Bre(b"forget").no_capture
    assert b == b"(?:forget)"
    assert type(b) is Bre


def test_string_atomic():
    b = Bre(b"content").atomic
    assert b == b"(?>content)"
    assert type(b) is Bre


def test_bytes_modify_flags():
    b = Bre(b"start").modify_flags(b"aiLmsux").append(b"end")
    assert b == b"start(?aiLmsux)end"
    assert type(b) is Bre


def test_bytes_named():
    b = Bre(b"content").named(b"label")
    assert b == b"(?P<label>content)"
    assert type(b) is Bre


def test_bytes_backreference():
    b = Bre(b"label").backreference
    assert b == b"(?P=label)"
    assert type(b) is Bre


def test_bytes_comment():
    b = Bre(b"important note").comment
    assert b == b"(?#important note)"
    assert type(b) is Bre


def test_bytes_followed_by():
    b = Bre(b"Isaac ").followed_by(b"Asimov")
    assert b == b"Isaac (?=Asimov)"
    assert type(b) is Bre


def test_bytes_not_followed_by():
    b = Bre(b"Isaac ").not_followed_by(b"Asimov")
    assert b == b"Isaac (?!Asimov)"
    assert type(b) is Bre


def test_bytes_preceded_by():
    b = Bre(b"chat").preceded_by(b"chit")
    assert b == b"(?<=chit)chat"
    assert type(b) is Bre


def test_bytes_not_preceded_by():
    b = Bre(b"chat").not_preceded_by(b"chit")
    assert b == b"(?<!chit)chat"
    assert type(b) is Bre


def test_bytes_yes_no():
    b = Bre.yes_no(1, b"yes")
    assert b == b"(?(1)yes)"
    assert type(b) is Bre
    c = Bre.yes_no(1, b"yes", b"no")
    assert c == b"(?(1)yes|no)"
    assert type(c) is Bre
    d = Bre.yes_no(b"label", b"yes")
    assert d == b"(?(label)yes)"
    assert type(d) is Bre
    e = Bre.yes_no(b"label", b"yes", b"no")
    assert e == b"(?(label)yes|no)"
    assert type(e) is Bre


def test_bytes_set():
    b = Bre(b"0-9a-f").set
    assert b == b"[0-9a-f]"
    assert type(b) is Bre


def test_bytes_optional():
    b = Bre(b"a").optional
    assert b == b"a?"
    c = Bre(b"ab").optional
    assert c == b"ab?"
    d = Bre(b"ab").unnamed.optional
    assert d == b"(ab)?"
    e = Bre(b"_").named(b"underscore").optional
    assert e == b"(?P<underscore>_)?"


def test_bytes_zero_or_more():
    b = Bre(b"a").zero_or_more
    assert b == b"a*"
    assert type(b) is Bre


def test_bytes_one_or_more():
    b = Bre(b"a").one_or_more
    assert b == b"a+"
    assert type(b) is Bre


def test_bytes_lazy():
    b = Bre(b"a").lazy
    assert b == b"a?"
    assert type(b) is Bre


def test_bytes_repeat():
    b = Bre(b"a").repeat(2)
    assert b == b"a{2,}"
    assert type(b) is Bre
    c = Bre(b"a").repeat(2, 3)
    assert c == b"a{2,3}"
    assert type(c) is Bre
    d = Bre(b"a").repeat(None, 3)
    assert d == b"a{,3}"
    assert type(d) is Bre
    e = Bre(b"a").repeat(2, None)
    assert e == b"a{2,}"
    assert type(e) is Bre
    f = Bre(b"a").repeat(None)
    assert f == b"a{,}"
    assert type(f) is Bre
    g = Bre(b"a").repeat(None, None)
    assert g == b"a{,}"
    assert type(g) is Bre


def test_bytes_compile():
    b = Bre(b"content").named(b"label")
    compiled = b.compile(Bre.I)
    assert isinstance(compiled, re.Pattern)
    assert compiled.pattern == b"(?P<label>content)"
    assert compiled.flags == Bre.I
