# This file was generated by jschema_to_python version 0.0.5.

class SarifLog(object):
    """Static Analysis Results Format (SARIF) Version 2.1.0-rtm.4 JSON Schema: a standard format for the output of static analysis tools."""
    def __init__(self,
        schemaUri=None,
        inlineExternalProperties=None,
        properties=None,
        runs=None,
        version=None):

        missing_properties = []
        if version is None:
            missing_properties.append('version')
        if runs is None:
            missing_properties.append('runs')
        if len(missing_properties) > 0:
            raise Exception('required properties of class SarifLog were not provided: {}'.format(', '.join(missing_properties)))

        self.schemaUri=schemaUri
        self.inlineExternalProperties=inlineExternalProperties
        self.properties=properties
        self.runs=runs
        self.version=version
