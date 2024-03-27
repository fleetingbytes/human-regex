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

re_functions = {
    "compile": re.compile,
    "search": re.search,
    "match": re.match,
    "fullmatch": re.fullmatch,
    "split": re.split,
    "findall": re.findall,
    "finditer": re.finditer,
    "sub": re.sub,
    "subn": re.subn,
    "escape": re.escape,
    "purge": re.purge,
}

re_proxy_class_dict.update({k: make_re_proxy_function(k, v) for k, v in re_functions.items()})

ReProxy = type("ReProxy", (), re_proxy_class_dict)
