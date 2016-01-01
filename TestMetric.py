class TestMetric :
    def __init__(self, obj) :
        self._func = obj
        self._Name = obj.__name__
        print("registering attribute %s" % self._Name)

    def __call__(self, obj = None) :
        # print("Attribute called " + self._Name)
        if obj != None :
            return self._func(obj)
        else :
            return self

    @property
    def Name(self) :
        print("Getting name for" + self._Name)
        return self._Name

#class TestLocator :
#    def __init__(self, obj)
