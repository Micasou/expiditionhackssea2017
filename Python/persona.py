from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
from PyDictionary import PyDictionary #pip install PyDictionary
class persona:
    def __init__(self, theName):
        self.name = theName
        self.articles = []  #list
        self.preference = {} #map
        self.mappedPreference = {}
    def addPreference(self, interest, value ):
        self.preference[interest] = value
    def checkArticleMatch(self, theArticle, list):
        if(personaConsumer(self, list)):
            self.articles.append(theArticle)
    def createMappedPreference(self):
        dictionary = PyDictionary()
        for key in self.preference:
            words = self.preference[key].split(" ")
            for word in words:
                synonymList = dictionary.synonym(word)
                synonymList.append(word)
                for syn in synonymList:
                    self.mappedPreference[syn] = self.preference[key]
    def personaConsumer(self, articleList):
        dictionary = PyDictionary()
        matchCountDict = {}
        for item in articleList:
            synonymList = dictionary.synonym(item)
            synonymList.append(item)
            for syn in synonymList:
                if (self.mappedPreference[syn] != null):
                    matchCountDict[self.mappedPreference[syn]] += 1
        return weighArticle(matchCountDict)
    def weighArticle(self, countMap):
        print ""