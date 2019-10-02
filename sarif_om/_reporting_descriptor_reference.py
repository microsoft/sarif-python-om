# This file was generated by jschema_to_python version 1.1.4.

import attr


@attr.s
class ReportingDescriptorReference(object):
    """Information about how to locate a relevant reporting descriptor."""

    guid = attr.ib(default=None, metadata={"schema_property_name": "guid"})
    id = attr.ib(default=None, metadata={"schema_property_name": "id"})
    index = attr.ib(default=-1, metadata={"schema_property_name": "index"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    tool_component = attr.ib(default=None, metadata={"schema_property_name": "toolComponent"})