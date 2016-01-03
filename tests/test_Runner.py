from pyxperiment.experiment import Experiment
from pyxperiment.registry import Registry
from pyxperiment.metric import Metric
from pyxperiment.runner import Runner

import unittest

import pyxperiment.tests.SimpleTest


class test_Runner(unittest.TestCase) :

    def test_Run(self) :

        simple_test = Registry.get('SimpleTest')

        runner = Runner()
        runner.add(simple_test)
        runner.run()
