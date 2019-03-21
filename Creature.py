import json

class Creature:
    def __init__(self, creatureJSON):
        self.__dict__ = json.loads(creatureJSON)
        terrainError = ValueError('A creatures terrains must be one of: "Land", "Water", or "Sky"')
        if not self.terrains:
            raise terrainError
        for terrain in self.terrains:
            if terrain != 'Land' or terrain != 'Water' or terrain != 'Sky':
                raise terrainError
    
    def __repr__(self):
        return 'Name: {}, CR: {}, Terrains: {}, Type: {}'.format(self.name, self.challengeRating, self.terrains, self.creatureType)