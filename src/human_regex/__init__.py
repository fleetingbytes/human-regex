from .contracts.general_regex import General_Regex_Base
from .contracts.building_blocks import create_property, building_blocks

# Classes String_Regex and Bytes_Regex are very similar.
# Bytes_Regex has a base class bytes rather than str
# and class properties made of building blocks
# which are encoded in UTF-8.
#
# Hence we generate these classes dynamically:
for class_name, str_or_bytes, encoding in (
    ("String_Regex", str, ""),
    ("Bytes_Regex", bytes, "utf-8"),
):
    globals()[class_name] = type(
        class_name,
        (str_or_bytes, General_Regex_Base),
        {k: create_property(v, encoding=encoding) for k, v in building_blocks.items()},
    )
