from src.ml_models import result
from src.ml_models import validator
from typing import List, Dict
#from sklearn.base import BaseEstimator

from .neural_network_estimator import WiEstimator as NeuralNetworkEstimator

NeuralNetworkParameters = [
    {
        "name": "solver",
        "type": str
    },
    {
        "name": "activation",
        "type": str
    },
    {
        "name": "max_iter",
        "type": int
    },
    {
        "name": "learning_rate_init",
        "type": float
    },
    {
        "name": "tol",
        "type": float
    },
    {
        "name": "hidden_layer_sizes",
        "type": List
    },
    {
        "name": "random_state",
        "type": int
    },
]

class NeuralNetworkValidator(validator.BaseValidator):
    def __init__(self, **kwargs):
        self.props = NeuralNetworkParameters
        validator.BaseValidator.doInit(self, **kwargs)

    def __call__(self):
        return_params = super(NeuralNetworkValidator, self).__call__()
        # additional validation goes here
        return return_params

class NeuralNetworkResult(result.SuccessResult):
    def __init__(self, *args, **kwargs):
        super(NeuralNetworkResult, self).__init__()
        for key, value in kwargs.items():
            self.add(key, value)

# class NeuralNetworkEstimator(WiEstimator):
  # Modify this class if you do not want to extend WiEstimator class
  # pass

