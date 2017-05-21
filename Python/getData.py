import json

def getReportsForPersona(persona):
    dataname = "../dataset/personaSamples.json"
    dataFile = open(dataname, 'r')
    data = json.loads(dataFile.read())
    datap = data[persona]
    reportsList = []
    articleList = []
    print 'start for'
    for path in datap['articles']:
        print path
        text = open('../dataset/' + path, 'r').read()
        lines = text.split('\n')
        print lines
        title = lines[0]
        body = '\n'.join(lines[1:]).strip()
        articleList.append({'title': title, 'text': body})
    print 'for loop end'
    if not articleList == []:
        reportsList.extend(articleList)
    result = {'phrases': (datap['phrases']).keys(), 'articles': reportsList}
    print 'result'
    return result