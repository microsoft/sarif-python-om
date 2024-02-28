# This file was generated by jschema_to_python version 1.2.3.

from ._location import Location
from ._property_bag import PropertyBag
from attrs import define
from attrs import field


@define()
class Suppression:
    """A suppression that is relevant to a result."""

    kind : str = field(metadata={"schema_property_name": "kind"})
    guid : str = field(default=None, metadata={"schema_property_name": "guid"})
    justification : str = field(default=None, metadata={"schema_property_name": "justification"})
    location : Location = field(default=None, metadata={"schema_property_name": "location"})
    properties : PropertyBag = field(default=None, metadata={"schema_property_name": "properties"})
    state : str = field(default=None, metadata={"schema_property_name": "state"})
