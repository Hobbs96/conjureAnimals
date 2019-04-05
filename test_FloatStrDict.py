from FloatStrDict import *
from collections import UserDict

def TestFloatStrDict():
    def test_initSimple(self):
        fSD = FloatStrDict()
        assert(isinstance(fSD, UserDict))

    def test_missing():
        fSD = FloatStrDict()
        fSD[7] = 4
        assert(fSD['7'] == 4)
        try:
            fSD['8']
        except:
            return
        assert(False)