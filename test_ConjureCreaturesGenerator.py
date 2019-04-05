from ConjureCreaturesGenerator import *
import pytest

class TestConjureCreaturesGenerator():
    def test_init_simple(self):
        generator = ConjureCreaturesGenerator('test_creatures.json')
        assert(len(generator.creaturesByCR) > 0)

    def test_call(self):
        generator = ConjureCreaturesGenerator('test_creatures.json')
        assert(len(generator(0, ['Land'])) > 0)

    def test_badCalls(self):
        generator = ConjureCreaturesGenerator('test_creatures.json')
        with pytest.raises(ValueError):
            generator(-1, ['Land'])
        with pytest.raises(ValueError):
            generator(0, [])
        with pytest.raises(ValueError):
            generator(0, ['Sand'])
    

    def test_readFromJSON(self):
        with pytest.raises(ValueError):
            generator = ConjureCreaturesGenerator('test_creatures.txt')
