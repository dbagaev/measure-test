from .metric import Metric

import inspect


class Experiment :
    def __init__(self, obj) :
        # This part creates new experiment as class decorator. In this case we have to register this class in the registry
        if inspect.isclass(obj):
            self._Class = obj
            self._Test = None
            self._Name = obj.__name__
            Registry.register(self)
        # This means that we instantiate experiment to run experiment passed
        elif obj is not None :
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

    def Metrics(self) :
        if self._Test is not None :
            tmp = self._Test
        else :
            tmp = self._Class()

        for mm in inspect.getmembers(tmp) :
            if isinstance(mm[1], Metric) :
                for m in mm[1].getChildMetrics() :
                    if m._Accumulator is None :
                        yield (m.Name, m)

    def __call__(self) :
        if self._Test == None :
            return self

        return self.run()


    def run(self) :
        self._Test.test()

'''
'''
class ExperimentSet:

    def __init__(self, exp):
        self._ExperimentClass = exp._Class

        self._Metrics = {}
        if exp._Test is not None :
            tmp = exp._Test
        else :
            tmp = exp._Class()

        for m in inspect.getmembers(tmp) :
            if isinstance(m[1], Metric) :
                for mm in m[1].getChildMetrics() :
                    if mm._Accumulator != None:
                        self._Metrics[mm.Name] = mm._Accumulator(mm)

        self._Experiments = []


    def addExperiment(self, experiment):
        if experiment._Class != self._ExperimentClass :
            return

        if experiment._Test is None :
            return

        self._Experiments.append(experiment)

        for m in inspect.getmembers(experiment._Test) :
            if isinstance(m[1], Metric) :
                for mm in m[1].getChildMetrics() :
                    if mm._Accumulator != None:
                        self._Metrics[mm.Name].add(mm)


    def Experiments(self):
        """Return experiments included this experiment set"""
        for t in self._Experiments:
            yield t

    def findExperiments(self):
        for t in self._ExperimentClass.findTests():
            yield Experiment(t)

    def Metrics(self):
        """Returns set metrics, e.g. metrics which have accumulators thus they are calculated entirely for the whole set"""
        for m in  self._Metrics.items() :
            yield m

    def run(self):
        for exp in self._Experiments :
            exp.run()

    @property
    def Name(self):
        return self._ExperimentClass.__name__

from .registry import Registry