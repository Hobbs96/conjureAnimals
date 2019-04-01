from ConjureCreaturesGenerator import *

class TestConjureCreaturesGenerator():
    def test_init_simple(self):
        generator = ConjureCreaturesGenerator('test_creatures.json')
        assert(len(generator.creaturesByCR) > 0)

    def test_call(self):
        generator = ConjureCreaturesGenerator('test_creatures.json')
        assert(len(generator(0, ['Land'])) > 0)

    def test_badCalls(self):
        generator = ConjureCreaturesGenerator('test_creatures.json')
        try:
            generator(-1, ['Land'])
        except Exception as e1:
            print(e1)
            try:
                generator(40, ['Land', 'Sky', 'Water'])
            except Exception as e2:
                print(e2)
                try:
                    generator(0, [])
                except Exception as e3:
                    print(e3)
                    return
        assert(False)
    

    def test_readFromJSON(self):
        try:
            generator = ConjureCreaturesGenerator('test_creatures.txt')
        except Exception as e:
            return
        assert(False)
