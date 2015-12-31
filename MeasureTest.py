import sys
import os
import inspect

class MeasuredTest :
    All = {}

    def __init__(self, obj) :
        self.obj = obj
        MeasuredTest.All[obj] = self

    def __call__(self) :
        print("Attribute called")

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
    def __init__(self) :
        self.data = ""

    def test(self) :
        print("DoTest.test()")


@MeasuredTest
class DoOtherTest :
    def __init__(self) :
        self.data = ""

    def test(self) :
        print("DoOtherTest.test()")

    @OutputParameter
    def Parameter1(self) :
        return 42

