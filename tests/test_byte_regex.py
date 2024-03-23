from human_regex.byte_regex import Byte_Regex as BR


def test_byte_regex():
    b = BR(b"hi")
    c = b.join(b" ", b"there")
    assert bytes(c) == b"hi there"
