from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .logistic_regression_classifier_estimator import WiEstimator as LogisticRegressionClassifierEstimator

LogisticRegressionClassifierParameters = [
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

class LogisticRegressionClassifierValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = LogisticRegressionClassifierParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(LogisticRegressionClassifierValidator, self).__call__()
        # additional validation goes here
        return return_params

class LogisticRegressionClassifierResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(LogisticRegressionClassifierResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class LogisticRegressionClassifierEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

