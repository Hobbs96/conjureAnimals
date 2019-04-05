from collections import UserDict

class FloatStrDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str) and '.' in key:
            raise KeyError(key)
        return self[str(float(key))]
    
    def __contains__(self, key):
        return str(float(key)) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(float(key))] = item