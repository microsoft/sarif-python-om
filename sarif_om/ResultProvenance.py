# This file was generated by jschema_to_python version 0.0.5.

class ResultProvenance(object):
    """Contains information about how and when a result was detected."""
    def __init__(self,
        conversionSources=[],
        firstDetectionRunGuid=None,
        firstDetectionTimeUtc=None,
        invocationIndex=-1,
        lastDetectionRunGuid=None,
        lastDetectionTimeUtc=None,
        properties=None):

        self.conversionSources=conversionSources
        self.firstDetectionRunGuid=firstDetectionRunGuid
        self.firstDetectionTimeUtc=firstDetectionTimeUtc
        self.invocationIndex=invocationIndex
        self.lastDetectionRunGuid=lastDetectionRunGuid
        self.lastDetectionTimeUtc=lastDetectionTimeUtc
        self.properties=properties
