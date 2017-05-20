class article:
    interests= {'interest' : 0.0}
    Relevance=0.0
    articleSource=""
    SourceType=0
    textSummary=""

    def addInterest(self, interest, likeness):
        interests[interest] = likeness

    def estimateRelevance(self, ):
        currentRelevance=0.0

        Relevance = currentRelevance

    def parseText(self, source, sourceType):
        if (sourceType == "website"):
            parseWebsie(source)
        elif (sourceType == "rawText"):
            print ""
        elif (sourceType == "localPath"):
            print ""

    def parseWebsie(self, source):
        #TODO get raw html
        print ""

    def parseRaw(self, rawText):
        #TODO parse raw
        print ""

    def parseFile(self, filePath):
        #TODO open file path
        print ""