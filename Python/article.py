class article:
    def __init__(self, articleText):
        self.tagMap= {'interest' : 0.0}
        self.Relevance= estimateRelevance(self, articleText)
        self.articleSource= ""
        self.textSummary= getSummary(self, articleText)
        self.timeStamp= getTimeStamp(articleText)
        getTags(self, articleText)

    def getTimeStamp(self, articleText):
        print "TODO finish"

    def estimateRelevance(self, articleText ):
        currentRelevance=0.0
        print "TODO finish"
        self.Relevance = currentRelevance

    def getSummary(self, articleText ):
        print "TODO finish"

    def getTags(self, articleText):
        self.tagMap["IMPLEMENT"] = "ADD MORE STUFF"
        print "TODO finish"