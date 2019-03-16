from collections import defaultdict
from random import randint
from fractions import Fraction
import json
import os

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
    
    def _readInFromFile(self, fileName):
        fileName, fileExtension = os.path.splitext(fileName)
        if (fileExtension == '.txt'):
            self._readFromTxtFile(fileName)
        elif (fileExtension == '.json'):
            self._readFromJSONFile(fileName)
        else:
            raise ValueError('The file type passed to the ConjureAnimalsGenerator must be ".txt" or ".json"')

    def _readFromTxtFile(self, fileName):
        with open(fileName + '.txt') as file:
            currentCR = 0
            for line in file:
                if line[0].isdigit():
                    currentCR = str(float(line))
                    print(currentCR)
                else:
                    self.animalsByCR[currentCR] += line.split(',')

    def _readFromJSONFile(self, fileName):
        # seems that this opens up to a lot of errors... what if the JSON passed in is poorly formatted?
        with open(fileName + '.json') as file:
            self.animalsByCR = json.load(file)

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
        if self.challengeRating <= 0.25:
            return self.animalsByCR['0.25'] + self.animalsByCR['0']
        else:
            return self.animalsByCR[str(self.challengeRating)]

    def _generateOutput(self):
        result = str()
        for key, value in self._generateAnimals().items():
            result += str(key).lstrip().rstrip() + ': ' + str(value) + '\n'
        return result

            
