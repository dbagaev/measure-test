from ..MeasuredTest  import MeasuredTest
import unittest


# And here come some unit tests

class TestSimpleTest(unittest.TestCase):
    def test_basic(self):
        for t in MeasuredTest.All:
            if t.typeName == 'SimpleTest':
                self.assertEquals(len(t.metrics()), 4)
