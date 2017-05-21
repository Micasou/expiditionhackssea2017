import os
import persona
import article
import operator
import json
import codecs

def generatePersonas():
    pesonaList = list()
    with open("../dataset/personaSamples.txt") as f:
        line = f.readline()
        while(line != ""):
            splitArray = line.split(",")
            #print line
            tempPersona = persona.persona(splitArray[0])
            #print len(splitArray)
            for item in splitArray:
                if item.find(":") != -1:
                    kvSplit = item.split(":")
                    tempPersona.addPreference(kvSplit[0], kvSplit[1])
                    #print kvSplit[0] + " is mapping to " + kvSplit[1]
            tempPersona.createMappedPreference()
            #print "Added a user " + tempPersona.name
            pesonaList.append(tempPersona)
            line = f.readline()
    return pesonaList
def addInterestToPersona(personaTitle, phrase, weight):
    print ""

def savePersonas(personas):
    file = open("savedPersonas.json", "rb+")
    file.write("[")
    for persona in personas:
        personaPreJson = dict()
        preferences = dict()
        articlePaths = dict()
        for key in persona.reversedMap: #create saved phrase preference that maps to synonyms
            preferences[key] = persona.reversedMap[key]
        personaPreJson["phrases"] = preferences
        personaPreJson["articles"] = persona.articles
        newThing  = dict()
        newThing[persona.name] = personaPreJson
        json_str = json.dumps(newThing)
        file.write(json_str)
        file.write(",")
    file.seek(-1, os.SEEK_END)
    file.truncate()
    file.write("]")
 
def isAscii(string):
    try:
        string.encode('ascii')
        return 1
    except:
        return 0

def main():
    personas = generatePersonas()
    #
    for subdir, dirs, files in os.walk("../dataset/articles/"):
        for file in files:
            filepath = subdir + os.sep + file
            print (file)
            if file != ".DS_Store":
                with codecs.open(filepath, "r",encoding='utf-8') as myfile:
                    wholeText = myfile.read()
                    print wholeText
                    for word in wholeText:
                        if not isAscii(word):
                            wholeText.replace(word, '')
                    arcl = article.article(wholeText, filepath)
                    for person in personas:
                        val = person.personaConsumer(arcl.tagList)
                        if val == 1:
                            person.articles.append(arcl)
    savePersonas(personas)
       # TODO once this loop finishes we will have a list of personas with data attached to them
       # TODO We need to store this data in a file, text, csv, doesnt matter, so that we can reduce processing time.
       # TODO Look at def generatePersonas function, you can basically do the same thing. but you also write to a file
       # TODO we also need to store articles so when we add a new user we can quickly query for what they would want in their feed
       # TODO The reading and writing should be a function of the front end using the data we've processed.

if __name__ == "__main__":
    main()