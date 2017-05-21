
class article:
    def __init__(self, articleText, articleName):
        self.dictionary = PyDictionary()
        self.tagList= []
        self.articleTitle= articleName
        self.articleSource= TextBlob(articleText)
        self.textSummary= self.getSummary(articleText)
        self.relevance= self.estimateRelevance(articleText)
        self.timeStamp= self.getTimeStamp()
        self.getTags(articleText)

    def getTimeStamp(articleText):
        print("TODO finish")

    def estimateRelevance(self, persona):
        currentRelevance=0.0
        #print "TODO finish"
        self.relevance = currentRelevance

    def getSummary(self, articleText):
        return self.articleSource[0:50]

    def getTags(self, articleText):
        for np in self.articleSource.noun_phrases:
            self.tagList.append(str(np))
            for val in (str(np).split()):
                synList = self.dictionary.synonym(val)
                if synList == []:
                    self.tagList.extend(synList)
        return self.tagList