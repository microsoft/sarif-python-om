# This file was generated by jschema_to_python version 0.0.5.

class ExternalPropertyFileReferences(object):
    """References to external property files that should be inlined with the content of a root log file."""
    def __init__(self,
        addresses=[],
        artifacts=[],
        conversion=None,
        driver=None,
        extensions=[],
        externalizedProperties=None,
        graphs=[],
        invocations=[],
        logicalLocations=[],
        policies=[],
        properties=None,
        results=[],
        taxonomies=[],
        threadFlowLocations=[],
        translations=[],
        webRequests=[],
        webResponses=[]):

        self.addresses=addresses
        self.artifacts=artifacts
        self.conversion=conversion
        self.driver=driver
        self.extensions=extensions
        self.externalizedProperties=externalizedProperties
        self.graphs=graphs
        self.invocations=invocations
        self.logicalLocations=logicalLocations
        self.policies=policies
        self.properties=properties
        self.results=results
        self.taxonomies=taxonomies
        self.threadFlowLocations=threadFlowLocations
        self.translations=translations
        self.webRequests=webRequests
        self.webResponses=webResponses
