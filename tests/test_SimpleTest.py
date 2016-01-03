from pyxperiment.experiment import Experiment, Registry
from pyxperiment.metric import Metric

import unittest

import pyxperiment.tests.SimpleTest

# And here come some unit tests

class TestSimpleTest(unittest.TestCase):
    def test_registration(self):
        simple_test = Registry.get('SimpleTest')
        self.assertIsNotNone(simple_test, "Experiment can't be located")

        metrics = list(simple_test.Metrics())
        self.assertEqual(len(metrics), 0)

        cases = list(simple_test.Experiments())
        self.assertEqual(len(cases), 3)
        simple_test = cases[0]

        metrics = {}
        for m in simple_test.Metrics():
            metrics[m.Name] = m
        self.assertEqual(len(metrics), 4)

        self.assertIn('Is', metrics)
        self.assertEqual(metrics['Is'].Type, Metric.TYPE_BOOLEAN)

        self.assertIn('Message', metrics)
        self.assertEqual(metrics['Message'].Type, Metric.TYPE_STRING)

        self.assertIn('Size', metrics)
        self.assertEqual(metrics['Size'].Type, Metric.TYPE_INTEGER)

        self.assertIn('Value', metrics)
        self.assertEqual(metrics['Value'].Type, Metric.TYPE_FLOAT)





