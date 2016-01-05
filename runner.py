from .experiment import Experiment, ExperimentSet
import copy

class RunnerResult:
    def __init__(self):
        self.SetResults = {}
        pass

class RunnerExperimentSetResult:
    def __init__(self, set):
        self.ExperimentResults = {}
        self.ExperimentSet = set
        self.Metrics = set.Metrics()
        pass

class RunnerExperimentResult:
    def __init__(self, experiment):
        self.Experiment = experiment
        self.Metrics = experiment.Metrics()

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
        exp_cls = experiment.__class__
        #e = Registry._ExperimentSets
        #for e in Registry():
        #    if e[0] == exp_cls :
        #        e = e[1]
        #        if e in self._ExperimentSets.keys():
        #            self._ExperimentSets[e].append(experiment)
        #        else:
        #            self._ExperimentSets[e] = [experiment]

    def _addExperiment(self, experiment):
        pass

    def _addExperimentSet(self, set):
        if not set in self._ExperimentSets :
            self._ExperimentSets[set.Name] = copy.copy(set)

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


