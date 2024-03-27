from human_regex import StringRegex as Sre
import re


def test_string_concatenate():
    s = Sre.concatenate(("a", "b", "c"))
    assert s == "abc"
    assert type(s) is Sre


def test_str_add():
    s = Sre("this") + " " + "and" + " " + "that"
    assert s == "this and that"
    assert type(s) is Sre
    s = Sre("this") + Sre(" ") + Sre("and") + Sre(" ") + Sre("that")
    assert s == "this and that"
    assert type(s) is Sre


def test_str_or():
    s = Sre("cyan") | "magenta" | "yellow" | "black"
    assert s == "cyan|magenta|yellow|black"
    assert type(s) is Sre


def test_string_append():
    s = Sre("hi")
    t = s.append(" ").append("there")
    assert t == "hi there"
    assert type(t) is Sre


def test_string_prepend():
    s = Sre("Party").prepend("Expected ").prepend("Long-").prepend("A ")
    assert s == "A Long-Expected Party"
    assert type(s) is Sre


def test_string_join():
    s = Sre(", ").join(("apples", "pears", "oranges"))
    assert s == "apples, pears, oranges"
    assert type(s) is Sre


def test_string_unnamed():
    s = Sre("content").unnamed
    assert s == "(content)"
    assert type(s) is Sre


def test_string_set_flags():
    s = Sre.set_flags("aiLmsux")
    assert s == "(?aiLmsux)"
    assert type(s) is Sre


def test_string_no_capture():
    s = Sre("forget").no_capture
    assert s == "(?:forget)"
    assert type(s) is Sre


def test_string_modify_flags():
    s = Sre("start").modify_flags("aiLmsux").append("end")
    assert s == "start(?aiLmsux)end"
    assert type(s) is Sre


def test_string_atomic():
    s = Sre("content").atomic
    assert s == "(?>content)"
    assert type(s) is Sre


def test_string_named():
    s = Sre("content").named("label")
    assert s == "(?P<label>content)"
    assert type(s) is Sre


def test_string_backreference():
    s = Sre("label").backreference
    assert s == "(?P=label)"
    assert type(s) is Sre


def test_string_comment():
    s = Sre("important note").comment
    assert s == "(?#important note)"
    assert type(s) is Sre


def test_string_followed_by():
    s = Sre("Isaac ").followed_by("Asimov")
    assert s == "Isaac (?=Asimov)"
    assert type(s) is Sre


def test_string_not_followed_by():
    s = Sre("Isaac ").not_followed_by("Asimov")
    assert s == "Isaac (?!Asimov)"
    assert type(s) is Sre


def test_string_preceded_by():
    s = Sre("chat").preceded_by("chit")
    assert s == "(?<=chit)chat"
    assert type(s) is Sre


def test_string_not_preceded_by():
    s = Sre("chat").not_preceded_by("chit")
    assert s == "(?<!chit)chat"
    assert type(s) is Sre


def test_string_yes_no():
    s = Sre.yes_no(1, "yes")
    assert s == "(?(1)yes)"
    assert type(s) is Sre
    t = Sre.yes_no(1, "yes", "no")
    assert t == "(?(1)yes|no)"
    assert type(t) is Sre
    u = Sre.yes_no("label", "yes")
    assert u == "(?(label)yes)"
    assert type(u) is Sre
    v = Sre.yes_no("label", "yes", "no")
    assert v == "(?(label)yes|no)"
    assert type(v) is Sre


def test_string_set():
    s = Sre("0-9a-f").set
    assert s == "[0-9a-f]"
    assert type(s) is Sre


def test_string_optional():
    s = Sre("a").optional
    assert s == "a?"
    t = Sre("ab").optional
    assert t == "ab?"
    u = Sre("ab").unnamed.optional
    assert u == "(ab)?"
    v = Sre("_").named("underscore").optional
    assert v == "(?P<underscore>_)?"


def test_string_zero_or_more():
    s = Sre("a").zero_or_more
    assert s == "a*"
    assert type(s) is Sre


def test_string_one_or_more():
    s = Sre("a").one_or_more
    assert s == "a+"
    assert type(s) is Sre


def test_string_lazy():
    s = Sre("a").lazy
    assert s == "a?"
    assert type(s) is Sre


def test_string_repeat():
    s = Sre("a").repeat(2)
    assert s == "a{2,}"
    assert type(s) is Sre
    t = Sre("a").repeat(2, 3)
    assert t == "a{2,3}"
    assert type(t) is Sre
    u = Sre("a").repeat(None, 3)
    assert u == "a{,3}"
    assert type(u) is Sre
    v = Sre("a").repeat(2, None)
    assert v == "a{2,}"
    assert type(v) is Sre
    w = Sre("a").repeat(None)
    assert w == "a{,}"
    assert type(w) is Sre
    x = Sre("a").repeat(None, None)
    assert x == "a{,}"
    assert type(x) is Sre


def test_string_compile():
    s = Sre("content").named("label")
    compiled = s.compile(Sre.I)
    assert isinstance(compiled, re.Pattern)
    assert compiled.pattern == "(?P<label>content)"
    assert compiled.flags == Sre.I | Sre.U
