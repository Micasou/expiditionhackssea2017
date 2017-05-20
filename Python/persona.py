class persona:
    def __init__(self):
        this.articles = [] #list
        this.preference = thePreference

    def __init__(self):
        this.articles = []  #list
        this.preference = {"string", 0.0} #map

    def addPreference(self, interest, value ):
        this.preference[interest] = value

    def attachArticle(self, theArticle):
        if(personaConsumer(self, theArticle)):
            this.articles.append(theArticle)
