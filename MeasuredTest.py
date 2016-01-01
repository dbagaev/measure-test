import inspect

from .TestMetric import TestMetric

class MeasuredTest :
    All = {}

    def __init__(self, obj) :
        self.obj = obj        
        MeasuredTest.All[obj] = self
        print("Registreing test: " + self.testType())

    def findTests(self) :
        print("Getting test list for " + self.testType())
        try :
            print(self.obj.findTests())
            return self.obj.findTests()
        except Exception as e:
            print(e)
            return []

    def testType(self) :
        return self.obj.__name__

    def metrics(self, obj = None) :
        if obj == None :
            tmp = self.obj()
        else :
            tmp = obj

        for m in inspect.getmembers(tmp) :
            if isinstance(m[1], TestMetric) :
                yield m[1]

    def __call__(self, obj = None) :
        if obj == None :
            return self

        obj.test()

        result = []

        for m in self.metrics(obj) :
            result.append((m.Name, m(obj), m))

        return result

