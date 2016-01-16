from .experiment import Experiment, ExperimentSet
import copy


class MetricValue :
    def __init__(self, metric, exp) :
        self._Metric = metric
        self._Experiment = exp

    @property
    def Name(self):
        return self._Metric.Name

    @property
    def Type(self) :
        return self._Metric.Type

    @property
    def Value(self) :
        return self._Metric(self._Experiment)

class RunnerResult :
    def __init__(self) :
        self.SetResults = {}
        pass


class RunnerExperimentSetResult:
    def __init__(self, set):
        self.ExperimentResults = {}
        self.ExperimentSet = set
        self.Metrics = {}

        for m in set.Metrics() :
            self.Metrics[m[0]] = MetricValue(m[1], set)


class RunnerExperimentResult:
    def __init__(self, experiment):
        self.Experiment = experiment
        self.Metrics = {}

        for m in experiment.Metrics :
            self.Metrics[m[0]] = MetricValue(m[1], experiment)


class Runner:
    def __init__(self):
        self._ExperimentSets = {}

    def add(self, experiment):
        if isinstance(experiment, Experiment) :
            self._addExperiment(experiment)
        elif isinstance(experiment, ExperimentSet) :
            self._addExperimentSet(experiment)
        else :
            return

    def _addExperiment(self, experiment):
        pass

    def _addExperimentSet(self, set):
        if not set.Name in self._ExperimentSets :
            exp_set = copy.copy(set)
            self._ExperimentSets[set.Name] = exp_set

    def run(self):

        result = RunnerResult()

        for set in self._ExperimentSets.items() :
            set_result = self._runSet(set[1])
            result.SetResults[set[0]] = set_result

        return result

    def _runSet(self, set):

        experiments = list(set.Experiments())
        if len(experiments) == 0 :
            for exp in set.findExperiments() :
                set.addExperiment(exp)
        experiments = list(set.Experiments())

        result = RunnerExperimentSetResult(set)

        for exp in experiments :
            try :
                result.ExperimentResults[exp.Name] = RunnerExperimentResult(exp)
                exp.run()
            except :
                pass

        return result


