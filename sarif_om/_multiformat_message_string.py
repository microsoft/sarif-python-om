# This file was generated by jschema_to_python version 1.2.3.

from ._property_bag import PropertyBag
from attrs import define
from attrs import field


@define()
class MultiformatMessageString:
    """A message string or message format string rendered in multiple formats."""

    text : str = field(metadata={"schema_property_name": "text"})
    markdown : str = field(default=None, metadata={"schema_property_name": "markdown"})
    properties : PropertyBag = field(default=None, metadata={"schema_property_name": "properties"})
