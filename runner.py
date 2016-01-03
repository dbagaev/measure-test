from .experiment import Experiment, ExperimentSet

class RunnerResult:
    def __init__(self):
        self.SetResults = {}
        pass

class RunnerExperimentSetResult:
    def __init__(self, set):
        self.ExperimentResults = {}
        self.ExperimentSet = set
        pass

class RunnerExperimentResult:
    def __init__(self):
        pass

class Runner:
    def __init__(self):
        self._ExperimentSets = {}

    def add(self, experiment):
        if experiment is Experiment :
            self._addExperiment(experiment)
        elif experiment is ExperimentSet :
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
            self._ExperimentSets[set] = []

        for exp in set.Experiments() :
            self._ExperimentSets[set].append(exp)

        pass

    def run(self):

        result = RunnerResult()

        for set in self._ExperimentSets.items() :
            set_result = self._runSet(set[0], set[1])
            result.SetResults.append(set_result)

        return result

    def _runSet(self, set, experiments):
        result = RunnerExperimentSetResult(set)

        for exp in experiments :
            exp_result = self._runExperiment(exp)
            result.ExperimentResults.append(exp_result)

        return result

    def _runExperiment(self, experiment):
        result = RunnerExperimentResult(experiment)

        return result


