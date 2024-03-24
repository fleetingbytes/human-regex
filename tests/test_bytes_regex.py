from human_regex import Bytes_Regex as Bre


def test_bytes_regex():
    b = Bre(b"hi")
    c = b.append(b" ", b"there")
    assert c == b"hi there"
