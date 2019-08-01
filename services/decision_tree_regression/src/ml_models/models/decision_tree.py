from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .decision_tree_estimator import WiEstimator as DecisionTreeEstimator

DecisionTreeParameters = [
    {
        "name": "criterion",
        "type": str
    },
    {
        "name": "splitter",
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
        "name": "random_state",
        "type": int
    },
]

class DecisionTreeValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = DecisionTreeParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(DecisionTreeValidator, self).__call__()
        # additional validation goes here
        return return_params

class DecisionTreeResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(DecisionTreeResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class DecisionTreeEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

