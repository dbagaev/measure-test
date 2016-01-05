from .metric import Metric

class MetricAccumulator:
    def __init__(self, metric) :
        self._Type = metric._Type
        self._Metrics = []

    def add(self, metric) :
        if metric._Type != self._Type :
            return
        self._Metrics.append(metric)


class Average(MetricAccumulator) :
    def __init__(self, metric) :
        super().__init__(metric)

    def __call__(self):
        if len(self._Metrics) == 0 :
            return 0

        value = 0
        for m in self._Metrics :
            value = value + m()

        return value / len(self._Metrics)


class Sum(MetricAccumulator) :
    def __init__(self, metric) :
        super().__init__(metric)

    def __call__(self):
        value = 0
        for m in self._Metrics :
            value = value + m()

        return value
