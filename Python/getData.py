import json

def getReportsForPersona(persona):
    dataname = "data.txt"
    dataFile = open(dataname, 'r')
    data = json.loads(dataFile.read())
    datap = data[persona]
    reportsList = []
    for phrase in datap:
        articleList = datap[phrase]['articles']
        if not articleList == []:
            reportsList.extend(articleList)
    return articleList

