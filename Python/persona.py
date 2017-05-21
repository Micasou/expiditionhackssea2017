from PyDictionary import PyDictionary#pip install PyDictionary
class persona:
    def __init__(self, theName):
        self.dictionary = PyDictionary()
        self.name = theName
        self.articles = list()  #list
        self.preference = dict()#map
        self.mappedPreference = dict()
    def printPreferences(self):
        for key in self.preference:
            print key
    def addPreference(self, interest, value ):
        self.preference[interest] = value
    def checkArticleMatch(self, theArticle, list):
        if(personaConsumer(self, list)):
            self.articles.append(theArticle)
    def createMappedPreference(self):
        for key in self.preference:
            #print "DA KEY IS: " + key
            words = key.split()
            #print words[0]
            for word in words:
                #print "Our word is: " + word
                synonymList = self.dictionary.synonym(word)
                if isinstance(synonymList, list):
                    synonymList.append(word)
                    for syn in synonymList:
                        self.mappedPreference[syn] = key
                        #print "New key: " + syn
    def weighArticle(self, countMap):
        print "TODO improve and use weight relevance to generate the rating."
        if len(countMap) > 0:
            return 1
        return 0
    def personaConsumer(self, articleList):
        matchCountDict = dict()
        for item in articleList:
            if (self.mappedPreference.get(item, "empty")!= "empty"):
                matchCountDict[self.mappedPreference[syn]] += 1
        return weighArticle(matchCountDict)
