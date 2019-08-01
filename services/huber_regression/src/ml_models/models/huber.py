from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .huber_estimator import WiEstimator as HuberEstimator

HuberParameters = [
    {
        "name": "epsilon",
        "type": float
    },
    {
        "name": "max_iter",
        "type": int
    },
    {
        "name": "alpha",
        "type": float
    },
    {
        "name": "tol",
        "type": float
    },
    {
        "name": "fit_intercept",
        "type": bool
    },
    {
        "name": "warm_start",
        "type": bool
    },
]

class HuberValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = HuberParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(HuberValidator, self).__call__()
        # additional validation goes here
        return return_params

class HuberResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(HuberResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class HuberEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

