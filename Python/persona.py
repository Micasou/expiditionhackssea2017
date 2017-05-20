class persona:
    def __init__(self, theName):
        this.name = theName
        this.articles = []  #list
        this.preference = {"string", 0.0} #map

    def addPreference(self, interest, value ):
        this.preference[interest] = value

    def attachArticle(self, theArticle):
        if(personaConsumer(self, theArticle)):
            this.articles.append(theArticle)
