# This file was generated by jschema_to_python version 0.0.5.

class ExternalPropertyFileReference(object):
    """Contains information that enables a SARIF consumer to locate the external property file that contains the value of an externalized property associated with the run."""
    def __init__(self,
        guid=None,
        itemCount=-1,
        location=None,
        properties=None):

        self.guid=guid
        self.itemCount=itemCount
        self.location=location
        self.properties=properties
