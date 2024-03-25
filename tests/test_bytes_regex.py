from human_regex import Bytes_Regex as Bre


def test_bytes_add():
    r = Bre(b"this") + b" " + b"and" + b" " + b"that"
    assert r == b"this and that"


def test_bytes_append():
    b = Bre(b"hi")
    c = b.append(b" ", b"there")
    assert c == b"hi there"
