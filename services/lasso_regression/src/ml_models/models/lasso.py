from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .lasso_estimator import WiEstimator as LassoEstimator

LassoParameters = [
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
        "name": "random_state",
        "type": int
    },
]

class LassoValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = LassoParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(LassoValidator, self).__call__()
        # additional validation goes here
        return return_params

class LassoResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(LassoResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class LassoEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

