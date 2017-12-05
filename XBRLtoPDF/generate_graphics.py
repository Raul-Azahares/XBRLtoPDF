from reportlab.graphics.charts.legends import Legend, TotalAnnotator
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from standard_colors import pdf_chart_colors, setItems
from reportlab.lib.validators import Auto
from reportlab.graphics.charts.barcharts import VerticalBarChart

class FactSheetHoldingsVBar(_DrawingEditorMixin,Drawing):
    def __init__(self,width=400,height=200,):
        Drawing.__init__(self, width, height)
        self._add(self,VerticalBarChart(),name='bar',validate=None,desc=None)


    def createGraphics(self,data,categoryNames,file):
        self.bar.data             = data
        self.bar.categoryAxis.categoryNames = categoryNames
        self.bar.categoryAxis.labels.fillColor = None
        self.bar.width                      = 160
        self.bar.height                     = 100
        self.bar.x                          = 30
        self.bar.y                          = 15
        self.bar.barSpacing                 = 5
        self.bar.groupSpacing               = 5
        self.bar.valueAxis.labels.fontName  = 'Helvetica'
        self.bar.valueAxis.labels.fontSize  = 6
        self.bar.valueAxis.forceZero        = 1
        self.bar.valueAxis.rangeRound       = 'both'
        self.bar.valueAxis.valueMax         = None#10#
        self.bar.categoryAxis.visible       = 1
        self.bar.categoryAxis.visibleTicks  = 0
        self.bar.barLabels.fontSize         = 6
        self.bar.valueAxis.labels.fontSize  = 6
        self.bar.strokeWidth                = 0.1
        self.bar.bars.strokeWidth           = 0.5
        n                                   = len(self.bar.data)
        setItems(n,self.bar.bars,'fillColor',pdf_chart_colors)
        #add and set up legend
        self._add(self,Legend(),name='legend',validate=None,desc=None)
        _ = ['Vodafone Group', 'UBS', 'British Petroleum', 'Royal bk of Scotland', 'HSBC Holdings', 'Total Elf Fina', 'Repsol', 'Novartis', 'BNP Paribas', 'Schneider Electric' ]
        self.legend.colorNamePairs  = [(Auto(chart=self.bar),(t,'%.2f'% d[0])) for t,d in zip(_,self.bar.data)]
        self.legend.columnMaximum   = 10
        self.legend.fontName        = 'Helvetica'
        self.legend.fontSize        = 5.5
        self.legend.boxAnchor       = 'w'
        self.legend.x               = 200
        self.legend.y               = self.height/4
        self.legend.dx              = 8
        self.legend.dy              = 8
        self.legend.alignment       = 'right'
        self.legend.yGap            = 0
        self.legend.deltay          = 11
        self.legend.dividerLines    = 1|2|4
        self.legend.subCols.rpad    = 10
        self.legend.dxTextSpace     = 3
        self.legend.strokeWidth     = 0
        self.legend.dividerOffsY    = 6
        self.legend.colEndCallout   = TotalAnnotator(rText='%.2f'%sum([x[0] for x in self.bar.data]), fontName='Helvetica-Bold', fontSize=self.legend.fontSize*1.1)
        self.legend.colorNamePairs  = [(self.bar.bars[i].fillColor, (self.bar.categoryAxis.categoryNames[i][0:20], '%0.2f' % self.bar.data[i][0])) for i in range(len(self.bar.data))]
        self.save(formats=['pdf'],outDir='graphics/'+file,fnRoot=None,)
# if __name__=="__main__": #NORUNTESTS
#     drawing = FactSheetHoldingsVBar()
#     drawing.save(formats=['pdf'],outDir='.',fnRoot=None,)
#     #drawing.save(formats=['png'],outDir='.',fnRoot=None)