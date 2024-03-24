from .contracts.general_regex import General_Regex_Base
from .contracts.primitives import create_property, primitives

for class_name, str_or_bytes, encoding in (
    ("String_Regex", str, ""),
    ("Bytes_Regex", bytes, "utf-8"),
):
    globals()[class_name] = type(
        class_name,
        (str_or_bytes, General_Regex_Base),
        {k: create_property(v, encoding=encoding) for k, v in primitives.items()},
    )
