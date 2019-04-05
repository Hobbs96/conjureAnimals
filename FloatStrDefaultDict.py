from FloatStrDict import FloatStrDict

class FloatStrDefaultDict(FloatStrDict):
    def __init__(self, defaultCallable):
        super().__init__()
        if not callable(defaultCallable):
            raise ValueError('defaultCallable must be a "callable" object')
        self._defaultFactory = defaultCallable

    def __getitem__(self, key):
        strFloatKey = str(float(key))
        if not key in self:
            self.data[strFloatKey] = self._defaultFactory()
        return self.data[strFloatKey]