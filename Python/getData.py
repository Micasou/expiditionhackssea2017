import json

def getReportsForPersona(persona):
    dataname = "data.txt"
    dataFile = open(dataname, 'r')
    data = json.loads(dataFile.read())
    datap = data[persona]
    reportsList = []
    for phrase in datap:
       articleList = []
        for path in datap[phrase]['articles']:
            article = open(path, 'r')
            articleList.append(article)
        if not articleList == []:
            reportsList.extend(articleList)
    return articleList

