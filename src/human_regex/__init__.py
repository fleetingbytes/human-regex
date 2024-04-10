"""
.. include:: ../../README.md
"""

from .bases import GeneralRegexBase, ReProxy
from .utilities import building_blocks, create_class_property

__all__ = ["StringRegex", "BytesRegex"]

# Classes StringRegex and BytesRegex are very similar.
# BytesRegex has a base class bytes rather than str
# and has class properties made of building blocks
# which are encoded in UTF-8, rather than Unicode strings.
#
# Hence we generate the classes StringRegex and BytesRegex dynamically:
for class_name, str_or_bytes, encoding in (
    ("StringRegex", str, ""),
    ("BytesRegex", bytes, "utf-8"),
):
    globals()[class_name] = type(
        class_name,
        (GeneralRegexBase, ReProxy, str_or_bytes),
        {k: create_class_property(v, encoding=encoding) for k, v in building_blocks.items()},
    )
