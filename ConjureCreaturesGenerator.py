from collections import defaultdict
from random import randint
import json
import os
from Creature import *

#TODO:rewrite the class with metadata config files to cover all of the non-specific conjure spells
#conjure woodland beings, minor elementals

class ConjureCreaturesGenerator:
    def __init__(self, fileName):
        self.creaturesByCR = defaultdict(list)
        self._readInFromFile(fileName)
        self.challengeRating = 0
    
    def __repr__(self):
        return self

    def __call__(self, challengeRating, terrains):
        errorStringMiddle = 'given to the ConjureCreaturesGenerator call must be'
        if challengeRating < 0:
            raise ValueError('Challenge rating ' + errorStringMiddle + ' >= 0')
        if not terrains:
            raise ValueError('Terrains collection ' + errorStringMiddle + ' non-empty')

        if challengeRating != 0:
            self.challengeRating = float(challengeRating)
        else:
            self.challengeRating == int(challengeRating)
        #TODO implement terrains checking with validTerrains.json
        self.terrains = set(terrains)
        return self._generateCreatures()
    
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

    def _generateOutput(self):
        result = str()
        for key, value in self._generateCreatures().items():
            result += str(key).lstrip().rstrip() + ': ' + str(value) + '\n'
        return result

            