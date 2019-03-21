class Creature:
    def __init__(self, name, challengeRating, terrains=["Land"], creatureType="Beast"):
        self.name = name
        self.challengeRating = challengeRating
        self.terrains = terrains
        self.creatureType = creatureType
    
    def __repr__(self):
        return 'Name: {}, CR: {}, Terrains: {}, Type: {}'.format(self.name, self.challengeRating, self.terrains, self.creatureType)