from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .decision_tree_classifier_estimator import WiEstimator as DecisionTreeClassifierEstimator

DecisionTreeClassifierParameters = [
    {
        "name": "criterion",
        "type": str
    },
    {
        "name": "min_samples_split",
        "type": int
    },
    {
        "name": "min_impurity_decrease",
        "type": float
    },
]

class DecisionTreeClassifierValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = DecisionTreeClassifierParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(DecisionTreeClassifierValidator, self).__call__()
        # additional validation goes here
        return return_params

class DecisionTreeClassifierResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(DecisionTreeClassifierResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class DecisionTreeClassifierEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

