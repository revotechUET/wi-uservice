from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .svm_estimator import WiEstimator as SVMEstimator

SVMParameters = [
    {
        "name": "kernel",
        "type": str
    },
    {
        "name": "degree",
        "type": int
    },
    {
        "name": "C",
        "type": float
    },
    {
        "name": "gamma",
        "type": float
    },
    {
        "name": "tol",
        "type": float
    },
    {
        "name": "max_iter",
        "type": int
    },
]

class SVMValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = SVMParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(SVMValidator, self).__call__()
        # additional validation goes here
        return return_params

class SVMResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(SVMResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class SVMEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

