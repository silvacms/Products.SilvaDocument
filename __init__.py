# Copyright (c) 2002-2004 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id: __init__.py,v 1.9 2004/07/22 16:41:19 faassen Exp $

from Products.Silva.ExtensionRegistry import extensionRegistry
from Products.Silva.ImporterRegistry import importer_registry
import EditorSupportNested
import ServiceCodeSourceCharset
import install

from Products.Silva.fssite import registerDirectory
from Products.SilvaMetadata.Compatibility import registerTypeForMetadata

from Products.SilvaDocument import Document

def initialize(context):
    from Products.SilvaDocument.silvaxml import xmlexport, xmlimport
    extensionRegistry.register(
        'SilvaDocument', 'Silva Document', context, [Document],
        install, depends_on='Silva')
    
    context.registerClass(
        EditorSupportNested.EditorSupport,
        constructors = (EditorSupportNested.manage_addEditorSupport, ),
        icon = "www/editorservice.gif"
        )
    
    context.registerClass(
        ServiceCodeSourceCharset.CodeSourceCharsetService,
        constructors = (ServiceCodeSourceCharset.manage_addCodeSourceCharsetServiceForm, 
                        ServiceCodeSourceCharset.manage_addCodeSourceCharsetService),
        icon = "www/editorservice.gif"
        )
    # old XML importer
    importer_registry.register_tag('silva_document', 	 
                                   Document.xml_import_handler)
    registerDirectory('views', globals())
    registerDirectory('widgets', globals())
    
    registerTypeForMetadata(Document.DocumentVersion.meta_type)

    initialize_upgrade()

    # new xml import/export
    xmlexport.initializeXMLExportRegistry()
    xmlimport.initializeXMLImportRegistry()

def initialize_upgrade():
    from Products.SilvaDocument import upgrade
    upgrade.initialize()

