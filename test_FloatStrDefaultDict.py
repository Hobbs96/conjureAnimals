from FloatStrDefaultDict import *
from collections import UserDict
import pytest

class TestFloatStrDictDefault():
    def test_initSimple(self):
        fSDD = FloatStrDefaultDict(list)
        assert(isinstance(fSDD, UserDict))
        assert(fSDD._defaultFactory == list)

        fSDD = FloatStrDefaultDict(dict)
        assert(fSDD._defaultFactory == dict)

        with pytest.raises(ValueError):
            fSDD = FloatStrDefaultDict([])
    
    def test_getitem(self):
        fSDD = FloatStrDefaultDict(list)
        fSDD[7].append(4)
        assert(fSDD['7'] == [4])
        fSDD[7.0].append(3)
        assert(fSDD[7.0] == [4, 3])
