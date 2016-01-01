class TestMetric :

    TYPE_UNKNOWN = -1
    TYPE_FLOAT = 0
    TYPE_INTEGER = 1
    TYPE_BOOLEAN = 2
    TYPE_STRING = 3
    TYPE_FILE = 4

    def __init__(self, obj=None, type=TYPE_UNKNOWN) :
        if obj != None :
            self._func = obj
            self._Name = obj.__name__
            print("registering attribute %s" % self._Name)
        else:
            self._func = None
            self._Name = "<Unknown>"

        self._Type = type

    def __call__(self, obj = None) :
        # print("Attribute called " + self._Name)
        if obj != None :
            if self._func == None:
                self._func = obj
                self._Name = obj.__name__
                print("registering attribute %s" % self._Name)
                return self
            else:
                return self._func(obj)
        else :
            return self

    @property
    def Name(self) :
        return self._Name

    @property
    def Type(self):
        return self._Type


#class TestLocator :
#    def __init__(self, obj)
