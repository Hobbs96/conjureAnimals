from collections import defaultdict
from random import randint
from fractions import Fraction
import json

class ConjureAnimalsGenerator:
    def __init__(self, fileName):
        self.animalsByCR = defaultdict(list)
        self._readInFromFile(fileName)
    
    def __repr__(self):
        pass

    def __call__(self, challengeRating):
        result = str()
        for key, value in self.generateAnimals(challengeRating).items():
            result += str(key).lstrip().rstrip() + ': ' + str(value) + '\n'
        return result
    
    def _readInFromFile(self, fileName):
        readFile = open(fileName, 'r')
        currentCR = 0
        for line in readFile:
            if line[0].isdigit():
                currentCR = Fraction(line)
            else:
                self.animalsByCR[currentCR] += line.split(',')
        readFile.close()

    def generateAnimals(self, challengeRating):
        if challengeRating > 0:
            numAnimals = min(2 // challengeRating, 8)
        else:
            numAnimals = 8
        animals = self.animalsByCR[challengeRating]
        results = defaultdict(int)

        for i in range(numAnimals):
            results[animals[randint(0, len(animals) - 1)]] += 1
        return results
