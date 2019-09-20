# This file was generated by jschema_to_python version 0.1.0.

class ToolComponent(object):
    """A component, such as a plug-in or the driver, of the analysis tool that was run."""
    def __init__(self,
        associatedComponent=None,
        contents=['localizedData', 'nonLocalizedData'],
        dottedQuadFileVersion=None,
        downloadUri=None,
        fullDescription=None,
        fullName=None,
        globalMessageStrings=None,
        guid=None,
        informationUri=None,
        isComprehensive=False,
        language='en-US',
        localizedDataSemanticVersion=None,
        locations=[],
        minimumRequiredLocalizedDataSemanticVersion=None,
        name=None,
        notifications=[],
        organization=None,
        product=None,
        productSuite=None,
        properties=None,
        releaseDateUtc=None,
        rules=[],
        semanticVersion=None,
        shortDescription=None,
        supportedTaxonomies=[],
        taxa=[],
        translationMetadata=None,
        version=None):

        missing_properties = []
        if name is None:
            missing_properties.append('name')
        if len(missing_properties) > 0:
            raise Exception('required properties of class ToolComponent were not provided: {}'.format(', '.join(missing_properties)))

        self.associatedComponent=associatedComponent
        self.contents=contents
        self.dottedQuadFileVersion=dottedQuadFileVersion
        self.downloadUri=downloadUri
        self.fullDescription=fullDescription
        self.fullName=fullName
        self.globalMessageStrings=globalMessageStrings
        self.guid=guid
        self.informationUri=informationUri
        self.isComprehensive=isComprehensive
        self.language=language
        self.localizedDataSemanticVersion=localizedDataSemanticVersion
        self.locations=locations
        self.minimumRequiredLocalizedDataSemanticVersion=minimumRequiredLocalizedDataSemanticVersion
        self.name=name
        self.notifications=notifications
        self.organization=organization
        self.product=product
        self.productSuite=productSuite
        self.properties=properties
        self.releaseDateUtc=releaseDateUtc
        self.rules=rules
        self.semanticVersion=semanticVersion
        self.shortDescription=shortDescription
        self.supportedTaxonomies=supportedTaxonomies
        self.taxa=taxa
        self.translationMetadata=translationMetadata
        self.version=version