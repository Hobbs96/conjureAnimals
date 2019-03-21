class Creature:
    def __init__(self, name, challengeRating, terrains=["Land"], creatureType="Beast"):
        self.name = name
        self.challengeRating = challengeRating

        terrainError = ValueError('A creatures terrains must be one of: "Land", "Water", or "Sky"')
        if not terrains:
            raise terrainError
        for terrain in terrains:
            if terrain != 'Land' or terrain != 'Water' or terrain != 'Sky':
                raise terrainError
                
        self.terrains = terrains
        self.creatureType = creatureType
    
    def __repr__(self):
        return 'Name: {}, CR: {}, Terrains: {}, Type: {}'.format(self.name, self.challengeRating, self.terrains, self.creatureType)