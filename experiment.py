from .metric import Metric

import inspect


class Experiment :
    def __init__(self, obj, name = None) :
        if inspect.isclass(obj):
            self._Class = obj
            self._Name = obj.__name__
            Registry.register(self)
        else:
            self._Class = obj.__class__
            self.obj = obj
            self._Name = name

    @property
    def Name(self):
        return self._Name

    def findTests(self) :
        print("Getting test list for " + self.testType())
        try :
            return self._Class.findTests()
        except Exception as e:
            print("Exception while locating tests: " + e)
            return []

    def testType(self) :
        return self._Class.__name__

    def Metrics(self, obj = None) :
        if obj == None :
            tmp = self._Class()
        else :
            tmp = obj

        for m in inspect.getmembers(tmp) :
            if isinstance(m[1], Metric) :
                yield m[1]

    def __call__(self, obj = None) :
        if obj == None :
            return self

        obj.test()

        result = []

        for m in self.metrics(obj) :
            result.append((m.Name, m(obj), m))

        return result

'''
'''
class ExperimentSet:

    def __init__(self, exp):
        self._Experiment = exp

    def Experiments(self):
        """Return experiments included this experiment set"""
        for t in self._Experiment.findTests():
            yield Experiment(t)

    def Metrics(self):
        """Returns set metrics, e.g. metrics which have accumulators thus they are calculated entirely for the whole set"""
        tmp = self._Experiment._Class()

        for m in inspect.getmembers(tmp) :
            if isinstance(m[1], Metric) and m[1]._Accumulator != None:
                yield m[1]


from .registry import Registry