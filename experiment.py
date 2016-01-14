from .metric import Metric

import inspect


class ExperimentSet:

    def __init__(self, exp):

        self._ExperimentClass = exp

        self._Metrics = {}
        for m in inspect.getmembers(exp) :
            if isinstance(m[1], Metric) :
                for mm in m[1].getChildMetrics() :
                    if mm._Accumulator != None:
                        self._Metrics[mm.Name] = mm._Accumulator(mm)

        self._Experiments = []


    def addExperiment(self, experiment):
        if experiment.__class__ != self._ExperimentClass :
            return

        self._Experiments.append(experiment)

        for m in inspect.getmembers(experiment) :
            if isinstance(m[1], Metric) :
                for mm in m[1].getChildMetrics() :
                    if mm._Accumulator != None:
                        self._Metrics[mm.Name].add(experiment)


    def Experiments(self):
        """Return experiments included this experiment set"""
        for t in self._Experiments:
            yield t

    def findExperiments(self):
        for t in self._ExperimentClass.findTests():
            yield t

    def Metrics(self):
        """Returns set metrics, e.g. metrics which have accumulators thus they are calculated entirely for the whole set"""
        for m in  self._Metrics.items() :
            yield m

    def AllMetrics(self):
        tmp = self._ExperimentClass()

        for m in inspect.getmembers(tmp) :
            if isinstance(m[1], Metric) :
                for mm in m[1].getChildMetrics() :
                    yield ( mm.Name, mm )


    def run(self):
        for exp in self._Experiments :
            exp.run()

    @property
    def Name(self):
        return self._ExperimentClass.__name__



class Registry:

    _Instance = None

    def __new__(cls, *args, **kwargs):
        if Registry._Instance is None:
            return super(Registry, cls).__new__(cls)
        else:
            return Registry._Instance

    def __init__(self):
        self._ExperimentSets = {}

    @staticmethod
    def getInstance():
        if Registry._Instance is None:
            Registry._Instance = Registry()

        return Registry._Instance

    @staticmethod
    def register(experiment):
        print("Registreing test: " + experiment.__name__)
        reg = Registry.getInstance()
        exp_set = ExperimentSet(experiment)
        reg._ExperimentSets[exp_set.Name] = exp_set

    @staticmethod
    def unregister(experiment):
        pass

    @staticmethod
    def get(name):
        if name in Registry.getInstance()._ExperimentSets.keys() :
            return Registry.getInstance()._ExperimentSets[name]
        else:
            return None


class ExperimentRegistrator(type) :
    def __init__(cls, name, bases, attrs) :
        try :
            if Experiment not in bases :
                return
        except :
            return

        Registry.register(cls)




class Experiment(metaclass=ExperimentRegistrator) :
    def __init__(self, obj) :
        if obj is not None :
            self._Class = obj.__class__
            self._Test = obj

            for mm in inspect.getmembers(obj) :
                if isinstance(mm[1], Metric) :
                    for m in mm[1].getChildMetrics() :
                        m._Self = obj

            self._Name = obj.Name
        else :
            raise Exception("Passing empty object to Experiment")

    @property
    def Name(self):
        if self._Test is not None :
            return self._Test.Name
        else :
            return None

    def findTests(self) :
        print("Getting test list for " + self.testType())
        try :
            return self._Class.findTests()
        except Exception as e:
            print("Exception while locating tests: " + e)
            return []

    @property
    def testType(self) :
        return self._Class.__name__

    def Metrics(self, filter = True) :
        for mm in inspect.getmembers(self.__class__) :
            if isinstance(mm[1], Metric) :
                for m in mm[1].getChildMetrics() :
                    if not filter or m._Accumulator is None :
                        yield (m.Name, m)

    def run(self) :
        pass

