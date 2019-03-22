from collections import defaultdict
from random import randint
import json
import os
from Creature import *

#TODO:rewrite the class with metadata config files to cover all of the non-specific conjure spells
#conjure woodland beings, minor elementals

class ConjureAnimalsGenerator:
    def __init__(self, fileName):
        self.animalsByCR = defaultdict(list)
        self._readInFromFile(fileName)
        self.challengeRating = 0
    
    def __repr__(self):
        pass

    def __call__(self, challengeRating):
        if challengeRating < 0:
            raise ValueError('Challenge rating given to the ConjureAnimalsGenerator call must be > 0')
        self.challengeRating = float(challengeRating)
        return self._generateAnimals()
    
    def _readInFromFile(self, filePath):
        fileName, fileExtension = os.path.splitext(filePath)
        if (fileExtension == '.txt'):
            self._readFromTxtFile(filePath)
        elif (fileExtension == '.json'):
            self._readFromJSONFile(filePath)
        else:
            raise ValueError('The file type passed to the ConjureAnimalsGenerator must be ".txt" or ".json"')

    def _readFromTxtFile(self, filePath):
        with open(filePath) as file:
            currentCR = 0
            for line in file:
                if line[0].isdigit():
                    currentCR = str(float(line))
                    print(currentCR)
                else:
                    self.animalsByCR[currentCR] += line.split(',')

    def _readFromJSONFile(self, filePath):
        with open(filePath) as file:
            data = json.load(file)
            for name, entry in data.items():
                if entry["Type"] == "Beast":
                    newCreature = asCreature(entry)
                    self.animalsByCR[entry['ChallengeRating']].append(newCreature)


    def _generateAnimals(self):
        if self.challengeRating > 0:
            numAnimals = min(2 // self.challengeRating, 8)
        else:
            numAnimals = 8
        numAnimals = int(numAnimals)

        animals = self._getAnimalSequence()
        animalCounts = defaultdict(int)

        for i in range(numAnimals):
            animalCounts[animals[randint(0, len(animals) - 1)]] += 1
        return animalCounts

    def _getAnimalSequence(self):
        # the number specifics should be moved out into a metadata file
        if self.challengeRating <= 0.25:
            return self.animalsByCR['0.25'] + self.animalsByCR['0.125'] + self.animalsByCR['0']
        else:
            return self.animalsByCR[str(self.challengeRating)]

    def _generateOutput(self):
        result = str()
        for key, value in self._generateAnimals().items():
            result += str(key).lstrip().rstrip() + ': ' + str(value) + '\n'
        return result

            
