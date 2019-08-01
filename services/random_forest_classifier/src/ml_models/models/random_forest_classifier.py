from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .random_forest_classifier_estimator import WiEstimator as RandomForestClassifierEstimator

RandomForestClassifierParameters = [
    {
        "name": "num_trees",
        "type": int
    },
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

class RandomForestClassifierValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = RandomForestClassifierParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(RandomForestClassifierValidator, self).__call__()
        # additional validation goes here
        return return_params

class RandomForestClassifierResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(RandomForestClassifierResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class RandomForestClassifierEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

