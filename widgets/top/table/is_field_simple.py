## Script (Python) "is_field_simple"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=node
##title=
##
elements = []
for child in node.childNodes:
    if child.nodeType == node.ELEMENT_NODE:
        elements.append(child)
if len(elements) != 1:
    return 0
return elements[0].nodeName == 'p'
