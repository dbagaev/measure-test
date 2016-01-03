from random import random

from pyxperiment.experiment import Experiment
from pyxperiment.metric import Metric

@Experiment
class SimpleTest:
    def __init__(self, name = ""):
        self.data = ""
        self._Name = name

        self._Size = 0
        self._Value = 0.1
        self._Is = True
        self._Message = ""

    def test(self):
        self._Size = 42
        self._Value = random()
        if random() < 0.1:
            self._Is = False
        else:
            self._Is = True
        self._Message = "Hey from test " + self.name
        print("DoOtherTest.test()")

    @classmethod
    def findTests(cls):
        return [cls("Case_000"), cls("Case_001"), cls("Case_002")]

    @Metric(type=Metric.TYPE_INTEGER)
    def Size(self):
        return self._Size

    @Metric(type=Metric.TYPE_FLOAT)
    def Value(self):
        return self._Value

    @Metric(type=Metric.TYPE_BOOLEAN)
    def Is(self):
        return self._Is

    @Metric(type=Metric.TYPE_STRING)
    def Message(self):
        return self._Message
