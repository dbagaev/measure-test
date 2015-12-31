import sys
import os
import inspect

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

class OutputParameter :
    def __init__(self, obj) :
        self.func = obj
        print("registering attribute %s" % obj.__name__)

    def __call__(self, obj) :
        print("Attribute " + self.func.__name__)
        return self.func(obj)

#class TestLocator :
#    def __init__(self, obj)


@MeasuredTest
class DoTest :
    def __init__(self, name) :
        self.data = ""
        self.name = name

    @classmethod
    def findTests(cls) :
        print("in DoTest.findTests()")
        return [cls('ghghgh')]

    def test(self) :
        print("DoTest.test()")


@MeasuredTest
class DoOtherTest :
    def __init__(self, name) :
        self.data = ""
        self.name = name

    def test(self) :
        print("DoOtherTest.test()")

    @classmethod
    def findTests(cls) :
        return [cls('asasas')]

    @OutputParameter
    def Parameter1(self) :
        return 42

