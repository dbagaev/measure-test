
class Metric :
    """Metric is any output value of the experiment.

    If Accumulator property of metric is set, then  metric value will be accumulated from distinct values of this metric
    of all test which belong to the set. For example, if your experiment calculates some value, our metric can measure
    average or total sum value of this value among all tests being executed."""
    TYPE_UNKNOWN = -1
    TYPE_FLOAT = 0
    TYPE_INTEGER = 1
    TYPE_BOOLEAN = 2
    TYPE_STRING = 3
    TYPE_FILE = 4

    def __init__(self, obj=None, name=None, type=TYPE_UNKNOWN, accumulator=None) :
        self.__name__ = None
        if obj != None :
            self.__name__ = obj.__name__
            self._func = obj
            if obj is not Metric :
                self._Name = obj.__name__
        else:
            self._func = None
            self._Name = "<Unknown>"
            self._Name = name

        self._Type = type
        self._Accumulator = accumulator
        if name is not None :
            self._Name = name
            self.__name__ = name

        self._Self = None

        self._ChildMetrics = [self]

        if obj is not None :
            print("registered attribute %s" % self._Name)

    def __call__(self, obj = None) :
        if obj is not None :
            if self._func is None:
                self._func = obj
                if self._Name is None :
                    self._Name = obj.__name__
                print("registered attribute %s" % self._Name)
                if self.__name__ is None :
                    self.__name__ = obj.__name__
                if isinstance(obj, Metric) :
                    self._ChildMetrics.append(obj)
                    if self._Type == Metric.TYPE_UNKNOWN :
                        self._Type = obj.Type
                return self
            else:
                return self._func(obj)
        else :
            if self._Self is None :
                return self
            else :
                return self._func(self._Self)

    def getChildMetrics(self):
        return self._ChildMetrics

    @property
    def Name(self) :
        return self._Name

    @property
    def Type(self):
        return self._Type

