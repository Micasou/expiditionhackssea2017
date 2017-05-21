def generatePersonas():
    personas=[]
    with open("../dataset/personaSamples.txt") as f:
        line = f.readline()
        splitArray = line.split(",")
        tempPersona = persona(splitArray[0])
        i = 1
        while i < len(splitArray):
            kvSplit = splitArray[i].split(":")
            tempPersona.preference[kvSplit[0]] = kvSplit[1]
        personas.append(tempPersona)
    return personas