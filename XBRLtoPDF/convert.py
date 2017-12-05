import preppy
import os
from rlextra.rml2pdf import rml2pdf
from diccionary import *
from generate_graphics import *

def main():

    data_graphics_one=[[4.22], [4.12], [3.65],[3.65],[3.65],[3.65]]
    categoryNames_graphics_one=['1','2','3',"4","5","6"]
    graphics_one = FactSheetHoldingsVBar()
    graphics_one.createGraphics(data_graphics_one,categoryNames_graphics_one,"graphics_one/")

    template = preppy.getModule('example_dos.prep')

    xbrl = os.path.dirname(os.path.dirname(__file__)) + "/Convertidor/xbrl/Anexo5FicS2.xbrl"
    xml_label_iic_fic = os.path.dirname(os.path.dirname(__file__)) + "/Convertidor/xbrl/iic-fic-2009-03-31-label.xml"
    xml_label_iic_com = os.path.dirname(os.path.dirname(__file__)) + "/Convertidor/xbrl/iic-com-2009-03-31-label.xml"

    documento = PDFOrder(xbrl,xml_label_iic_fic,xml_label_iic_com)

    lista_elementos= documento.fechDiccionari()

    rmlText = template.get(lista_elementos)

    pdfFileName = "pdf/documento" + '.pdf'
    rml2pdf.go(rmlText, outputFileName=pdfFileName)


if __name__=='__main__':
    main()