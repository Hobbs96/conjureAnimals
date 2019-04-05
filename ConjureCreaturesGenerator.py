from collections import defaultdict
from random import randint
import json
import os
from Creature import *

#TODO:rewrite the class to handle all of the various conjuration spells without loading multiple files

class ConjureCreaturesGenerator:
    def __init__(self, fileName):
        #TODO subclass a dictionary so that one can access elements with a string, int, or float key (pg. 80 in Fluent Python)
        self.creaturesByCR = defaultdict(list)
        self._readInFromFile(fileName)
        self.challengeRating = 0
    
    def __repr__(self):
        return self

    def __call__(self, challengeRating, terrains):
        self.validateCallInput(challengeRating, terrains)
        if challengeRating != 0:
            self.challengeRating = float(challengeRating)
        else:
            self.challengeRating == int(challengeRating)
        self.terrains = set(terrains)
        return self._generateCreatures()

    def validateCallInput(self, challengeRating, terrains):
        errorStringMiddle = 'given to the ConjureCreaturesGenerator call must be'
        if challengeRating < 0:
            raise ValueError('Challenge rating ' + errorStringMiddle + ' >= 0')
        if not terrains:
            raise ValueError('Terrains collection ' + errorStringMiddle + ' non-empty')
        #TODO the below code is hard-coded, although the values therein aren't expected to change. Fix necessary?
        try:
            validTerrainsFile = open('validTerrains.json')
            validTerrains = set(json.load(validTerrainsFile)["ValidTerrains"])
        except:
            raise ValueError('Failed to load validTerrains.json file')
        if not validTerrains.intersection(terrains):
            raise ValueError('All entries in the terrains sequence ' + errorStringMiddle + ' "Air", "Land", or "Water"')
    
    def _readInFromFile(self, filePath):
        fileName, fileExtension = os.path.splitext(filePath)
        if (fileExtension == '.json'):
            self._readFromJSONFile(filePath)
        else:
            raise ValueError('The file type passed to the ConjureCreaturesGenerator must be ".json"')

    def _readFromJSONFile(self, filePath):
        with open(filePath) as file:
            data = json.load(file)
            for key, lst in data.items():
                for entry in lst:
                    newCreature = asCreature(entry)
                    self.creaturesByCR[entry['ChallengeRating']].append(newCreature)

    def _generateCreatures(self):
        if self.challengeRating > 0:
            numCreatures = min(2 // self.challengeRating, 8)
        else:
            numCreatures = 8
        numCreatures = int(numCreatures)

        creatures = self._getCreatureSequence()
        creatureCounts = defaultdict(int)

        for i in range(numCreatures):
            creatureCounts[creatures[randint(0, len(creatures) - 1)]] += 1
        return creatureCounts

    def _getCreatureSequence(self):
        # the number specifics should be moved out into a metadata file
        if str(self.challengeRating) not in self.creaturesByCR:
            raise KeyError('This generator object has no creatures of the requested Challenge Rating')

        if self.challengeRating <= 0.25:
            sequence = self.creaturesByCR['0.25'] + self.creaturesByCR['0.125'] + self.creaturesByCR['0']
        else:
            sequence = self.creaturesByCR[str(self.challengeRating)]
            
        return [creature for creature in sequence if set(creature.terrains).intersection(self.terrains)]

            
