from reportlab.lib.colors import HexColor

pdf_chart_colors = [ HexColor("#01C0F4"), HexColor("#00AFEE"), HexColor("#0176A1"), HexColor("#025A7E"), HexColor("#0B3F7B"), HexColor("#0B3F7B"), HexColor("#eb8585"), HexColor("#e04747"), HexColor("#d60a0a"), HexColor("#cc0000"), HexColor("#ff0000"), ]
#pdf_chart_colors = [ HexColor("#01C0F4"), HexColor("#00AFEE"), HexColor("#0176A1"), HexColor("#025A7E"), HexColor("#0B3F7B"),]

def setItems(n, obj, attr, values):
    m = len(values)
    i = m // n
    for j in xrange(n):
        setattr(obj[j],attr,values[j*i % m])