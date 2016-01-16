from pyxperiment.experiment import Experiment, Registry
from pyxperiment.metric import Metric
from pyxperiment.runner import Runner

import unittest

import pyxperiment.tests.SimpleTest


class test_Runner(unittest.TestCase) :

    def test_Run(self) :
        simple_test = Registry.get('SimpleTest')

        #for exp in simple_test.findExperiments() :
        #    simple_test.addExperiment(exp)

        #simple_test.run()

