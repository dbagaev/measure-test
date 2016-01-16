from pyxperiment.experiment import Experiment, Registry
from pyxperiment.metric import Metric, MetricSet

import unittest

import pyxperiment.tests.SimpleTest

# And here come some unit tests

class TestMetricSet(unittest.TestCase):
    def setUp(self) :
        self.Test = pyxperiment.tests.SimpleTest.SimpleTest()
        self.Test.run()

    def test_filters(self) :
        m_set = MetricSet(self.Test, MetricSet.INCLUDE_ALL)
        self.assertEquals(len(m_set), 6)

        m_set = MetricSet(self.Test, MetricSet.INCLUDE_NON_ACCUMULATORS)
        self.assertEquals(len(m_set), 4)

        m_set = MetricSet(self.Test, MetricSet.INCLUDE_ACCUMULATORS)
        self.assertEquals(len(m_set), 2)

        m_set = MetricSet(self.Test, MetricSet.INCLUDE_NONE)
        self.assertEquals(len(m_set), 0)

    def test_iterative(self) :
        m_set = MetricSet(self.Test, MetricSet.INCLUDE_NON_ACCUMULATORS)
        cnt = 0
        size_found = False
        for m in m_set :
            cnt += 1
            if m[0] == 'Size' :
                self.assertEquals(42, m_set.Size)
                size_found = True

        self.assertEquals(4, cnt)
        self.assertTrue(size_found)

