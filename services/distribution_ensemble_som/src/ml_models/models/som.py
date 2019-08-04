from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .som_estimator import WiEstimator as SOMEstimator

SOMParameters = [
    {
        "name": "n_estimators",
        "type": int
    },
    {
        "name": "size_of_estimator",
        "type": int
    },
    {
        "name": "random_state",
        "type": int
    }
]

class SOMValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = SOMParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(SOMValidator, self).__call__()
        # additional validation goes here
        return return_params

class SOMResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(SOMResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class SOMEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass
