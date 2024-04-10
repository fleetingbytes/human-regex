def create_class_property(constant, encoding):
    maybe_encoded = constant
    if encoding:
        maybe_encoded = str.encode(constant, encoding=encoding)

    @classmethod
    @property
    # ruff: noqa: ARG001
    def func(cls):
        return maybe_encoded

    return func


building_blocks = {
    "EMPTY": "",
    "OPEN_CHAR_SET": "[",
    "CLOSE_CHAR_SET": "]",
    "OPEN_GROUP": "(",
    "CLOSE_GROUP": ")",
    "OPEN_EXTENSION": "(?",
    "CLOSE_EXTENSION": ")",
    "OPEN_NAME": "P<",
    "CLOSE_NAME": ">",
    "OPEN_QUANTIFIER": "{",
    "CLOSE_QUANTIFIER": "}",
    "QUANTIFIER_SEPARATOR": ",",
    "OR": "|",
    "NO_CAPTURE": ":",
    "FLAGS_END": ":",
    "ATOMIC": ">",
    "NAME_REFERENCE": "P=",
    "COMMENT": "#",
    "FOLLOWED_BY": "=",
    "NOT_FOLLOWED_BY": "!",
    "PRECEDED_BY": "<=",
    "NOT_PRECEDED_BY": "<!",
    "ZERO_OR_MORE": "*",
    "ONE_OR_MORE": "+",
    "OPTIONAL": "?",
    "LAZY": "?",
}


def make_re_proxy_function(func):
    def proxied(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        return result

    proxied.__doc__ = f"Proxy for re.{func.__name__}\n" + func.__doc__
    return proxied
