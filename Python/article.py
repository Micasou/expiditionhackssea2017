class article:
    def __init__(self):
        self.interests= {'interest' : 0.0}
        self.Relevance=0.0
        self.articleSource=""
        self.SourceType=0
        self.textSummary=""

    def addInterest(self, interest, likeness):
        self.interests[interest] = likeness

    def estimateRelevance(self, ):
        currentRelevance=0.0
        self.Relevance = currentRelevance

    def parseText(self, sourcePath):
        #TODO call the class
