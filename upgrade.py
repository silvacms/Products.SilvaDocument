# zope imports
import zLOG

# silva imports
from Products.Silva.interfaces import IUpgrader
from Products.Silva import upgrade

from Products.SilvaDocument.Document import Document, DocumentVersion

class SwitchClass:
    
    __implements__ = IUpgrader

    def __init__(self, new_class, args=(), kwargs={}):
        self.new_class = new_class
        self.args = args
        self.kwargs = kwargs

    def upgrade(self, obj):
        obj_id = obj.getId()
        new_obj = self.new_class(obj_id, *self.args, **self.kwargs)
        new_obj.__dict__.update(obj.__dict__)
        container = obj.aq_parent
        setattr(container, obj_id, new_obj)
        new_obj = getattr(container, obj_id)
        return new_obj
   
    def __repr__(self):
        return "<SwitchClass %r>" % self.new_class

class UpgradeDocumentXML:

    __implements__ = IUpgrader

    def upgrade(self, obj):
        # <index name="foo">bar</index> to
        # bar<index name="foo"/> 
        dom = obj.content
        node = dom.firstChild
        while node:
            if node.nodeType == node.ELEMENT_NODE and node.nodeName == 'index':
                while node.firstChild:
                    node.parentNode.insertBefore(node.firstChild, node)
            next = node.firstChild
            if not next:
                next = node.nextSibling
            if not next:
                next = node.parentNode.nextSibling
            node = next
        return obj

def initialize():
    upgrade.registry.registerUpgrader(SwitchClass(Document),
        '0.9.3', Document.meta_type)
    upgrade.registry.registerUpgrader(SwitchClass(DocumentVersion,
        args=('', )), '0.9.3', DocumentVersion.meta_type)
    upgrade.registry.registerUpgrader(UpgradeDocumentXML(), '0.9.3',
        DocumentVersion.meta_type)

