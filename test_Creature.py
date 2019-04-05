from Creature import *
import pytest

class TestCreature():
    def test_initSimple(self):
        frog = Creature('Frog', '0.25')
        assert(frog.name == 'Frog')
        assert(frog.challengeRating == '0.25')
        assert(frog.terrains == ['Land'])
        assert(frog.creatureType == 'Beast')
    
    def test_initKeywords(self):
        demonFish = Creature('Demon Fish', '1', terrains=['Water'], creatureType='Monstrosity')
        assert(demonFish.terrains == ['Water'])
        assert(demonFish.creatureType == 'Monstrosity')

    def test_initBadTerrains(self):
        with pytest.raises(ValueError):
            spaceCreature = Creature('SpaceCreature', '1', terrains=['Space'])

    def test_repr(self):
        dog = Creature('Doggo', '1')
        assert(str(dog) == "(Name: Doggo, CR: 1, Terrains: ['Land'], Type: Beast)")
            
        
