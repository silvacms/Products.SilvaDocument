# This module contains code to integrate the SilvaExternalSources extension
# with the SilvaDocument extension. The Document and its widgets make use
# of this module instead of directly using the SilvaExternalSources code.
try:
    from Products.SilvaExternalSources import ExternalSource
    AVAILABLE = 1
except ImportError:
    AVAILABLE = 0
    
    def availableSources(context):
        return []
    
    def getSourceForId(context, id):
        return None
    
    def isSourceCacheable(context, node):
        return 1
    
    def getSourceParameters(context, node):
        return {}
else:
    availableSources = ExternalSource.availableSources
    getSourceForId = ExternalSource.getSourceForId
    from _externalsource import getSourceParameters, isSourceCacheable
    