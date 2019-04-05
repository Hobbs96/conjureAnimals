from FloatStrDict import *
from collections import UserDict
import pytest

class TestFloatStrDict():
    def test_initSimple(self):
        fSD = FloatStrDict()
        assert(isinstance(fSD, UserDict))

    def test_missing(self):
        fSD = FloatStrDict()
        fSD[7] = 4
        with pytest.raises(KeyError):
            fSD['8']

    def test_contains(self):
        fSD = FloatStrDict()
        fSD[7] = 1
        assert('7.0' in fSD and 7.0 in fSD and '7' in fSD and 7 in fSD)
        assert('8.0' not in fSD and 8.0 not in fSD and '8' not in fSD and 8 not in fSD)

    def test_setitem(self):
        fSD = FloatStrDict()
        fSD[7] = 1
        assert(fSD[7.0] == 1 and fSD[7] == 1)
        assert(fSD['7'] == 1 and fSD['7.0'] == 1)
