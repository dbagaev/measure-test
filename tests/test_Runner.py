from pyxperiment.experiment import Experiment, Registry
# from pyxperiment.registry import Registry
from pyxperiment.metric import Metric
from pyxperiment.runner import Runner

import unittest

import pyxperiment.tests.SimpleTest


class test_Runner(unittest.TestCase) :

    def test_Run(self) :

        simple_test = Registry.get('SimpleTest')

        runner = Runner()
        runner.add(simple_test)
        result = runner.run()

        self.assertEquals(len(result.SetResults), 1)

        set_results = result.SetResults['SimpleTest']
        self.assertEquals(len(set_results.ExperimentResults), 3)

        for m in set_results.Metrics :
            if m[0] == 'TotalSize' :
                self.assertEquals(m[1](), 126)
            elif m[1] == 'AvgVaue' :
                self.assertLessEqual(m[1](), 1.)
