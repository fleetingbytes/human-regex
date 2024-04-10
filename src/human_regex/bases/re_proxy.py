import re

from ..utilities import create_class_property, make_re_proxy_function

re_flags = {
    "A": re.A,
    "ASCII": re.ASCII,
    "DEBUG": re.DEBUG,
    "I": re.I,
    "IGNORECASE": re.IGNORECASE,
    "L": re.L,
    "LOCALE": re.LOCALE,
    "M": re.M,
    "MULTILINE": re.MULTILINE,
    "NOFLAG": re.NOFLAG,
    "S": re.S,
    "DOTALL": re.DOTALL,
    "U": re.U,
    "UNICODE": re.UNICODE,
    "X": re.X,
    "VERBOSE": re.VERBOSE,
}

re_proxy_class_dict = {k: create_class_property(v, encoding=None) for k, v in re_flags.items()}

re_functions = [
    re.compile,
    re.search,
    re.match,
    re.fullmatch,
    re.split,
    re.findall,
    re.finditer,
    re.sub,
    re.subn,
    re.escape,
    re.purge,
]

re_proxy_class_dict.update({f.__name__: make_re_proxy_function(f) for f in re_functions})
re_proxy_class_dict.update({"RegexFlag": re.RegexFlag})

ReProxy = type("ReProxy", (), re_proxy_class_dict)
