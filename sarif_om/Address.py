# This file was generated by jschema_to_python version 0.0.5.

class Address(object):
    """A physical or virtual address, or a range of addresses, in an 'addressable region' (memory or a binary file)."""
    def __init__(self,
        absoluteAddress=-1,
        fullyQualifiedName=None,
        index=-1,
        kind=None,
        length=None,
        name=None,
        offsetFromParent=None,
        parentIndex=-1,
        properties=None,
        relativeAddress=None):

        self.absoluteAddress=absoluteAddress
        self.fullyQualifiedName=fullyQualifiedName
        self.index=index
        self.kind=kind
        self.length=length
        self.name=name
        self.offsetFromParent=offsetFromParent
        self.parentIndex=parentIndex
        self.properties=properties
        self.relativeAddress=relativeAddress
