from .metric import Metric

class MetricAccumulatorException(Exception) :
    pass

class MetricAccumulator:
    def __init__(self, metric) :
        self._Name = metric.Name
        self._Metric = metric
        self._Metrics = []
        self._Type = metric._Type

    def __call__(self, obj = None) :
        return self.calculate()

    def add(self, exp) :
        # TODO : Check if exp has this metric as member
        self._Metrics.append(exp)

    @staticmethod
    def _convertToNumeric(val):
        if isinstance(val, bool) :
            if val : return 1
            else : return 0
        elif not isinstance(val, (int, float)) :
            raise Exception("Invlide metric value '%s'" % str(v) )
        return val


    @property
    def Type(self) :
        return self._Type

    @property
    def Name(self) :
        return self._Name


class Average(MetricAccumulator) :
    def __init__(self, metric) :
        super().__init__(metric)
        if metric.Type != Metric.TYPE_FLOAT and metric.Type != Metric.TYPE_INTEGER and metric.Type != Metric.TYPE_BOOLEAN :
            raise MetricAccumulatorException("Type is not suitable for average accumulation")
        self._Type = Metric.TYPE_FLOAT

    def calculate(self):
        if len(self._Metrics) == 0 :
            return 0

        value = 0
        for m in self._Metrics :
            v = MetricAccumulator._convertToNumeric(self._Metric(m))
            value = value + v

        return value / len(self._Metrics)


class Sum(MetricAccumulator) :
    def __init__(self, metric) :
        super().__init__(metric)
        if metric.Type == Metric.TYPE_BOOLEAN :
            self._Type == Metric.TYPE_INTEGER
        elif metric.Type != Metric.TYPE_FLOAT and metric.Type != Metric.TYPE_INTEGER :
            raise MetricAccumulatorException("Type is not suitable for sum accumulation")


    def calculate(self):
        value = 0
        for m in self._Metrics :
            v = MetricAccumulator._convertToNumeric(self._Metric(m))
            value = value + v

        return value
