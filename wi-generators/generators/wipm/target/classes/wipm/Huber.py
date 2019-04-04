from src.ml_models import result
from src.ml_models import validator
from sklearn.linear_model import HuberRegressor


HuberParameters = [{
    "name": "epsilon",
    "type": float
}, {
    "name": "max_iter",
    "type": int
}, {
    "name": "alpha",
    "type": float
}, {
    "name": "tol",
    "type": float
}]


class HuberValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        global HuberParameters
        self.props = HuberParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(HuberValidator, self).__call__()
        # additional validation goes here

        return return_params


class HuberResult(result.SuccessResult):
    def __init__(self, mean_squared_error, mean_absolute_error, *args, **kwargs):
        super(HuberResult, self).__init__()
        self.add("mean_squared_error", mean_squared_error)
        self.add("mean_absolute_error", mean_absolute_error)


class HuberEstimator(HuberRegressor):
    pass

