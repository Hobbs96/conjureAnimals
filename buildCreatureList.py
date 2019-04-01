from Creature import *
import json

def buildBeastList(file):
    newFile = open('newCreatures.json', 'a')
    newFile.write('{"Beasts":[\n')
    with open(file) as jsonFile:
        data = json.load(jsonFile)
        for key, entry in data.items():
            newFile.write(asJSONString(asCreature(entry)))
            newFile.write(',\n') # issue here with a trailing comma
    newFile.write(']}')
    newFile.close()

