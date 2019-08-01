from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .xgboost_estimator import WiEstimator as XgboostEstimator

XgboostParameters = [
    {
        "name": "n_estiamtors",
        "type": int
    },
    {
        "name": "max_depth",
        "type": int
    },
    {
        "name": "gamma",
        "type": float
    },
    {
        "name": "booster",
        "type": str
    },
    {
        "name": "reg_alpha",
        "type": float
    },
    {
        "name": "reg_lamda",
        "type": float
    },
    {
        "name": "random_state",
        "type": int
    },
]

class XgboostValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = XgboostParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(XgboostValidator, self).__call__()
        # additional validation goes here
        return return_params

class XgboostResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(XgboostResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class XgboostEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

