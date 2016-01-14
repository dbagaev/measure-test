from .metric import Metric

class MetricAccumulator:
    def __init__(self, metric) :
        self._Name = metric.Name
        self._Metric = metric
        self._Metrics = []

    def add(self, exp) :
        # TODO : Check if exp has this metric as member
        self._Metrics.append(exp)

    @property
    def Type(self) :
        return self._Type

    @property
    def Name(self) :
        return self._Name


class Average(MetricAccumulator) :
    def __init__(self, metric) :
        super().__init__(metric)

    def __call__(self):
        if len(self._Metrics) == 0 :
            return 0

        value = 0
        for m in self._Metrics :
            value = value + self._Metric(m)

        return value / len(self._Metrics)


class Sum(MetricAccumulator) :
    def __init__(self, metric) :
        super().__init__(metric)

    def __call__(self):
        value = 0
        for m in self._Metrics :
            value = value + self._Metric(m)

        return value
