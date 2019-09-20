# This file was generated by jschema_to_python version 0.0.5.

class MultiformatMessageString(object):
    """A message string or message format string rendered in multiple formats."""
    def __init__(self,
        markdown=None,
        properties=None,
        text=None):

        missing_properties = []
        if text is None:
            missing_properties.append('text')
        if len(missing_properties) > 0:
            raise Exception('required properties of class MultiformatMessageString were not provided: {}'.format(', '.join(missing_properties)))

        self.markdown=markdown
        self.properties=properties
        self.text=text
