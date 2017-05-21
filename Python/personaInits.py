import os
import persona
import article

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

def main():
    personas = generatePersonas()
    for subdir, dirs, files in os.walk("../dataset/articles/"):
        for file in files:
            filepath = subdir + os.sep + file
            print (file)
            if file != ".DS_Store":
                print "yo"
                with open(filepath) as myfile:
                    wholeText = myfile.read()
                    print wholeText
                    arcl = article.article(wholeText, file)
                    for person in personas:
                        val = person.personaConsumer(arcl.tagList)
                        if val == 1:
                            person.articles.append(arcl)

if __name__ == "__main__":
    main()