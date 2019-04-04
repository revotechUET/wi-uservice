import secrets

from src import model_helper as helper
from src import config
from src import ml_models

from .create import *


@helper.parse_body_request
def train(model_id, features, target):
    try:
        result_ml = helper.model_train(model_id, features, target)
    except Exception as err:
        config.logger.error(str(err))
        err_message = ml_models.result.ErrorResult()
        return err_message()
    else:
        success_message = ml_models.get_result(model_id)(**result_ml)
        return success_message()


@helper.parse_body_request
def predict(model_id, features):
    try:
        target = helper.model_predict(model_id, features)
    except Exception as err:
        config.logger.error(str(err))
        err_message = ml_models.result.ErrorResult()
        return err_message()
    else:
        success_message = ml_models.result.SuccessResult()
        success_message.add("target", target)
        return success_message()

