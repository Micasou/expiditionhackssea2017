import json

def getReportsForPersona(persona):
    dataname = "../dataset/personaSamples.json"
    dataFile = open(dataname, 'r')
    data = json.loads(dataFile.read())
    datap = data[persona]
    reportsList = []
    articleList = []
    print "got to here!"
    for path in datap['articles']:
        article = open(path, 'r')
        articleList.append(article)
    print 'after for loop'
    if not articleList == []:
        reportsList.extend(articleList)
    print 'return value', reportsList
    return reportsList

