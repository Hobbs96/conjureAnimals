import json
from Creature import *


def convertToCreatures(file):
    with open(file) as jsonFile:
        data = json.load(jsonFile)
        with open('creatures.json', 'a') as writeFile:
            writeFile.write('{\n')
            for cR, creatureList in data.items():
                for creature in creatureList:
                    writeFile.write(asJSONString(Creature(creature, cR)))
            writeFile.write('}')


