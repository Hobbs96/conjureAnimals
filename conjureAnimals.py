from collections import defaultdict
from random import randint
from fractions import Fraction

class ConjureAnimalsGenerator:
    def __init__(self, fileName):
        self.animalsByCR = defaultdict(list)
        self._readInFromFile(fileName)
    
    def __repr__(self):
        pass

    def __call__(self, challengeRating):
        try:
            challengeRating = Fraction(challengeRating)
            if challengeRating < 0:
                raise ValueError
        except Exception as e:
            raise ValueError('The value passed to a ConjureAnimalsGenerator call must be a number or fractional string >= 0')
        self.challengeRating = challengeRating
        return self._generateAnimals()
    
    def _readInFromFile(self, fileName):
        readFile = open(fileName, 'r')
        currentCR = 0
        for line in readFile:
            if line[0].isdigit():
                currentCR = Fraction(line)
            else:
                self.animalsByCR[currentCR] += line.split(',')
        readFile.close()

    def _generateAnimals(self):
        if self.challengeRating > 0:
            numAnimals = min(2 // self.challengeRating, 8)
        else:
            numAnimals = 8

        animals = self._getAnimalSequence()
        animalCounts = defaultdict(int)

        for i in range(numAnimals):
            animalCounts[animals[randint(0, len(animals) - 1)]] += 1
        return animalCounts

    def _getAnimalSequence(self):
        if self.challengeRating <= 0.25:
            return self.animalsByCR[0.25] + self.animalsByCR[0]
        else:
            return self.animalsByCR[self.challengeRating]

    def _generateOutput(self):
        result = str()
        for key, value in self._generateAnimals().items():
            result += str(key).lstrip().rstrip() + ': ' + str(value) + '\n'
        return result

            
