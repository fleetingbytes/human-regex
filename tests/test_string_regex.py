from human_regex.string_regex import String_Regex as Sre


def test_string_regex():
    s = Sre("hi")
    t = s.append(" ", "there")
    assert t == "hi there"
