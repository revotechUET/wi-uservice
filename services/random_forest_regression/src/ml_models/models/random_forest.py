from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .random_forest_estimator import WiEstimator as RandomForestEstimator

RandomForestParameters = [
    {
        "name": "n_estimators",
        "type": int
    },
    {
        "name": "criterion",
        "type": str
    },
    {
        "name": "max_depth",
        "type": int
    },
    {
        "name": "max_features",
        "type": int
    },
    {
        "name": "bootstrap",
        "type": bool
    },
    {
        "name": "random_state",
        "type": int
    },
]

class RandomForestValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = RandomForestParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(RandomForestValidator, self).__call__()
        # additional validation goes here
        return return_params

class RandomForestResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(RandomForestResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class RandomForestEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

