from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .neural_network_classifier_estimator import WiEstimator as NeuralNetworkClassifierEstimator

NeuralNetworkClassifierParameters = [
    {
        "name": "hidden_layer_sizes",
        "type": List
    },
    {
        "name": "activation",
        "type": str
    },
    {
        "name": "algorithm",
        "type": str
    },
    {
        "name": "num_epochs",
        "type": int
    },
    {
        "name": "optimizer",
        "type": str
    },
    {
        "name": "learning_rate",
        "type": float
    },
    {
        "name": "warm_up",
        "type": bool
    },
    {
        "name": "decay",
        "type": float
    },
    {
        "name": "population",
        "type": int
    },
    {
        "name": "sigma",
        "type": float
    },
    {
        "name": "boosting_ops",
        "type": int
    },
]

class NeuralNetworkClassifierValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = NeuralNetworkClassifierParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(NeuralNetworkClassifierValidator, self).__call__()
        # additional validation goes here
        return return_params

class NeuralNetworkClassifierResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(NeuralNetworkClassifierResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class NeuralNetworkClassifierEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

