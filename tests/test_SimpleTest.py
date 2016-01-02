from ..Experiment  import Experiment
import unittest


# And here come some unit tests

class TestSimpleTest(unittest.TestCase):
    def test_basic(self):
        for t in Experiment.All:
            if t.typeName == 'SimpleTest':
                self.assertEquals(len(t.metrics()), 4)
