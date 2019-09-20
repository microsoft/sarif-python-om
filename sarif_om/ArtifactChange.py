# This file was generated by jschema_to_python version 0.1.0.

class ArtifactChange(object):
    """A change to a single artifact."""
    def __init__(self,
        artifactLocation=None,
        properties=None,
        replacements=None):

        missing_properties = []
        if artifactLocation is None:
            missing_properties.append('artifactLocation')
        if replacements is None:
            missing_properties.append('replacements')
        if len(missing_properties) > 0:
            raise Exception('required properties of class ArtifactChange were not provided: {}'.format(', '.join(missing_properties)))

        self.artifactLocation=artifactLocation
        self.properties=properties
        self.replacements=replacements