from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .non_linear_regressor_estimator import WiEstimator as NonLinearRegressorEstimator

NonLinearRegressorParameters = [
    {
        "name": "string_function",
        "type": str
    },
    {
        "name": "varialbes",
        "type": List
    },
    {
        "name": "parameters",
        "type": List
    },
]

class NonLinearRegressorValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = NonLinearRegressorParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(NonLinearRegressorValidator, self).__call__()
        # additional validation goes here
        return return_params

class NonLinearRegressorResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(NonLinearRegressorResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class NonLinearRegressorEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

