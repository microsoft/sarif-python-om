# This file was generated by jschema_to_python version 0.0.5.

class Stack(object):
    """A call stack that is relevant to a result."""
    def __init__(self,
        frames=None,
        message=None,
        properties=None):

        missing_properties = []
        if frames is None:
            missing_properties.append('frames')
        if len(missing_properties) > 0:
            raise Exception('required properties of class Stack were not provided: {}'.format(', '.join(missing_properties)))

        self.frames=frames
        self.message=message
        self.properties=properties
