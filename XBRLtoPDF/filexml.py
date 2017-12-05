
from xml.etree import ElementTree


class XMLParser(object):

    def __init__(self, precision=0):
        self.precision = precision

    @classmethod
    def parse(self, file_handle):
        """
        parse is the main entry point for an XMLParser. It takes a file
        handle.
        """
        xml = ElementTree.parse(file_handle)
        return xml

    @classmethod
    def MethodGeneric(self,
                    xml,
                    data_name,
                    ignore_errors=0
                     ):
        """
        Parse company custom entities from XML and return an Custom object.
        """
        text=""
        for node in xml.iter():
            if (node.attrib.get('id') == data_name):
                text= node.text
            else:
                pass
        return text
