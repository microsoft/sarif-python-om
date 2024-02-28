# This file was generated by jschema_to_python version 1.2.3.

from ._message import Message
from ._property_bag import PropertyBag
from attrs import define
from attrs import field


@define()
class Edge:
    """Represents a directed edge in a graph."""

    id : str = field(metadata={"schema_property_name": "id"})
    source_node_id : str = field(metadata={"schema_property_name": "sourceNodeId"})
    target_node_id : str = field(metadata={"schema_property_name": "targetNodeId"})
    label : Message = field(default=None, metadata={"schema_property_name": "label"})
    properties : PropertyBag = field(default=None, metadata={"schema_property_name": "properties"})
