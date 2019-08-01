from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .logistic_regression_tree_classifier_estimator import WiEstimator as LogisticRegressionTreeClassifierEstimator

LogisticRegressionTreeClassifierParameters = [
    {
        "name": "c",
        "type": float
    },
    {
        "name": "max_iter",
        "type": int
    },
    {
        "name": "solver",
        "type": str
    },
]

class LogisticRegressionTreeClassifierValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = LogisticRegressionTreeClassifierParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(LogisticRegressionTreeClassifierValidator, self).__call__()
        # additional validation goes here
        return return_params

class LogisticRegressionTreeClassifierResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(LogisticRegressionTreeClassifierResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class LogisticRegressionTreeClassifierEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

