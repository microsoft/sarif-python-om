# This file was generated by jschema_to_python version 0.0.5.

class Region(object):
    """A region within an artifact where a result was detected."""
    def __init__(self,
        byteLength=None,
        byteOffset=-1,
        charLength=None,
        charOffset=-1,
        endColumn=None,
        endLine=None,
        message=None,
        properties=None,
        snippet=None,
        sourceLanguage=None,
        startColumn=None,
        startLine=None):

        self.byteLength=byteLength
        self.byteOffset=byteOffset
        self.charLength=charLength
        self.charOffset=charOffset
        self.endColumn=endColumn
        self.endLine=endLine
        self.message=message
        self.properties=properties
        self.snippet=snippet
        self.sourceLanguage=sourceLanguage
        self.startColumn=startColumn
        self.startLine=startLine
