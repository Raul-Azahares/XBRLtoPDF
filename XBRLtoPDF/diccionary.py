from filexbrl import *
from filexml import *




class PDFOrder(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, xbrl_file, xml_label_iic_fic_file,xml_label_iic_com_file):
        """Constructor"""
        self.xbrl_file = xbrl_file
        self.xml_label_iic_fic_file = xml_label_iic_fic_file
        self.xml_label_iic_com_file = xml_label_iic_com_file

        xbrl_parser = XBRLParser(precision=0)
        xbrl = xbrl_parser.parse(xbrl_file)
        self.xbrl_obj = xbrl

        xml_label_parser = XMLParser(precision=0)
        xml_label_iic_fic = xml_label_parser.parse(open(xml_label_iic_fic_file))
        self.xml_label_iic_fic_obj = xml_label_iic_fic

        xml_label_parser = XMLParser(precision=0)
        xml_label_iic_com = xml_label_parser.parse(open(xml_label_iic_com_file))
        self.xml_label_iic_com_obj = xml_label_iic_com

    def fechDiccionari(self):

        xbrl_parser = XBRLParser(precision=0)
        xml_label_iic_fic_parser = XMLParser(precision=0)
        xml_label_iic_com_parser = XMLParser(precision=0)
        diccionario = {

            "registrocnmv":xbrl_parser.RegistroCNMV(self.xbrl_obj)[0]['datatext'],
            "AnoInforme":xbrl_parser.MethodGeneric(self.xbrl_obj, 'iic-com:AnoInforme'),
            "RatingDepositario":xbrl_parser.MethodGeneric(self.xbrl_obj, 'iic-com:RatingDepositario')



        }

        return diccionario

