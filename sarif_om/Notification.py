# This file was generated by jschema_to_python version 0.1.0.

class Notification(object):
    """Describes a condition relevant to the tool itself, as opposed to being relevant to a target being analyzed by the tool."""
    def __init__(self,
        associatedRule=None,
        descriptor=None,
        exception=None,
        level='warning',
        locations=[],
        message=None,
        properties=None,
        threadId=None,
        timeUtc=None):

        missing_properties = []
        if message is None:
            missing_properties.append('message')
        if len(missing_properties) > 0:
            raise Exception('required properties of class Notification were not provided: {}'.format(', '.join(missing_properties)))

        self.associatedRule=associatedRule
        self.descriptor=descriptor
        self.exception=exception
        self.level=level
        self.locations=locations
        self.message=message
        self.properties=properties
        self.threadId=threadId
        self.timeUtc=timeUtc