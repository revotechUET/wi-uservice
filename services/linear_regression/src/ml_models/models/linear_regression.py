from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .linear_regression_estimator import WiEstimator as LinearRegressionEstimator

LinearRegressionParameters = [
    {
        "name": "fit_intercept",
        "type": bool
    },
    {
        "name": "normalize",
        "type": bool
    },
]

class LinearRegressionValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = LinearRegressionParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(LinearRegressionValidator, self).__call__()
        # additional validation goes here
        return return_params

class LinearRegressionResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(LinearRegressionResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class LinearRegressionEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

