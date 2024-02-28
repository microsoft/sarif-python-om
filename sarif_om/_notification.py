# This file was generated by jschema_to_python version 1.2.3.

from ._exception import Exception
from ._location import Location
from ._message import Message
from ._property_bag import PropertyBag
from ._reporting_descriptor_reference import ReportingDescriptorReference
from attrs import define
from attrs import field


@define()
class Notification:
    """Describes a condition relevant to the tool itself, as opposed to being relevant to a target being analyzed by the tool."""

    message : Message = field(metadata={"schema_property_name": "message"})
    associated_rule : ReportingDescriptorReference = field(default=None, metadata={"schema_property_name": "associatedRule"})
    descriptor : ReportingDescriptorReference = field(default=None, metadata={"schema_property_name": "descriptor"})
    exception : Exception = field(default=None, metadata={"schema_property_name": "exception"})
    level : str = field(default="warning", metadata={"schema_property_name": "level"})
    locations : list[Location] = field(factory=list, metadata={"schema_property_name": "locations"})
    properties : PropertyBag = field(default=None, metadata={"schema_property_name": "properties"})
    thread_id : int = field(default=None, metadata={"schema_property_name": "threadId"})
    time_utc : str = field(default=None, metadata={"schema_property_name": "timeUtc"})
