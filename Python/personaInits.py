import os
import persona
import article

def generatePersonas():
    pesonaList = list()
    with open("../dataset/personaSamples.txt") as f:
        line = f.readline()
        while(line != ""):
            splitArray = line.split(",")
            print line
            tempPersona = persona.persona(splitArray[0])
            print len(splitArray)
            for item in splitArray:
                if item.find(":") != -1:
                    kvSplit = item.split(":")
                    tempPersona.addPreference(kvSplit[0], kvSplit[1])
                    print kvSplit[0] + " is mapping to " + kvSplit[1]
            tempPersona.printPreferences()
            tempPersona.createMappedPreference()
            print "Added a user " + tempPersona.name
            pesonaList.append(tempPersona)
            line = f.readline()
    return pesonaList

def main():
    personas = generatePersonas()
    for person in personas:
        print person.name
    for subdir, dirs, files in os.walk("../dataset/articles/"):
        for file in files:
            filepath = subdir + os.sep + file
            print (filepath)
            with open(filepath) as file:
                wholeText = file.readlines()
                print wholeText

if __name__ == "__main__":
    main()