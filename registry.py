from .experiment import ExperimentSet

class Registry:

    _Instance = None

    def __new__(cls, *args, **kwargs):
        if Registry._Instance is None:
            return super(Registry, cls).__new__(cls)
        else:
            return Registry._Instance

    def __init__(self):
        self._ExperimentSets = {}

    @staticmethod
    def getInstance():
        if Registry._Instance is None:
            Registry._Instance = Registry()

        return Registry._Instance

    @staticmethod
    def register(experiment):
        print("Registreing test: " + experiment.testType)
        reg = Registry.getInstance()
        reg._ExperimentSets[experiment.testType] = ExperimentSet(experiment)

    @staticmethod
    def unregister(experiment):
        pass

    @staticmethod
    def get(name):
        if name in Registry.getInstance()._ExperimentSets.keys() :
            return Registry.getInstance()._ExperimentSets[name]
        else:
            return None
