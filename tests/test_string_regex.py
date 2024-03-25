from human_regex import String_Regex as Sre


def test_str_add():
    r = Sre("this") + " " + "and" + " " + "that"
    assert r == "this and that"


def test_string_append():
    s = Sre("hi")
    t = s.append(" ", "there")
    assert t == "hi there"
    assert type(t) is Sre


def test_string_join():
    s = Sre("-").join(("a", "b", "c"))
    assert s == "a-b-c"
    assert type(s) is Sre
