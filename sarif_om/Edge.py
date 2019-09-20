# This file was generated by jschema_to_python version 0.1.0.

class Edge(object):
    """Represents a directed edge in a graph."""
    def __init__(self,
        id=None,
        label=None,
        properties=None,
        sourceNodeId=None,
        targetNodeId=None):

        missing_properties = []
        if id is None:
            missing_properties.append('id')
        if sourceNodeId is None:
            missing_properties.append('sourceNodeId')
        if targetNodeId is None:
            missing_properties.append('targetNodeId')
        if len(missing_properties) > 0:
            raise Exception('required properties of class Edge were not provided: {}'.format(', '.join(missing_properties)))

        self.id=id
        self.label=label
        self.properties=properties
        self.sourceNodeId=sourceNodeId
        self.targetNodeId=targetNodeId