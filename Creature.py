import json

class Creature:
    def __init__(self, name, challengeRating, terrains=["Land"], creatureType="Beast"):
        self.name = name
        self.challengeRating = challengeRating

        terrainError = ValueError('All of a creatures terrains must be one of: "Land", "Water", or "Sky",' +
        'and it must have at least one')
        if not terrains:
            raise terrainError
        for terrain in terrains:
            if terrain != 'Land' and terrain != 'Water' and terrain != 'Sky':
                raise terrainError
                
        self.terrains = terrains
        self.creatureType = creatureType
    
    def __repr__(self):
        return '(Name: {}, CR: {}, Terrains: {}, Type: {})'.format(self.name, self.challengeRating, self.terrains, self.creatureType)

#invoke as creature = Creature(json.loads(jsonObject, object_hook = asCreature))
def asCreature(dictionary):
    return Creature(dictionary['Name'], dictionary['ChallengeRating'],
     dictionary.get('Terrains', None), dictionary.get('Type', None))


def asJSONString(creature):
    elements = dict()
    elements["Name"] = creature.name
    elements["ChallengeRating"] = creature.challengeRating
    elements['Terrains'] = creature.terrains
    elements['Type'] = creature.creatureType
    result = json.dumps(elements, indent=4)
    return result