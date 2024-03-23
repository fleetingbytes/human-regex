from human_regex.string_regex import String_Regex as SR


def test_string_regex():
    s = SR("hi")
    t = s.join(" ", "there")
    assert str(t) == "hi there"
