import secrets

from src import model_helper as helper
from src import config
from src import ml_models

from .create import *
from .data import get_data_by_bucket_id
import numpy as np
import traceback

@helper.parse_body_request
def train(model_id, features, target):
    features = np.array(features).T
    target = np.array(target)
    try:
        result_ml = helper.model_train(model_id, features, target)
    except Exception as err:
        config.logger.error(str(err))
        config.logger.error(traceback.print_exc())
        err_message = ml_models.result.ErrorResult()
        return err_message()
    else:
        success_message = ml_models.get_result(model_id)(**result_ml)
        return success_message()


@helper.parse_body_request
def predict(model_id, features):
    features = np.array(features).T
    try:
        target = helper.model_predict(model_id, features)
    except Exception as err:
        config.logger.error(str(err))
        config.logger.error(traceback.print_exc())
        err_message = ml_models.result.ErrorResult()
        return err_message()
    else:
        success_message = ml_models.result.SuccessResult()
        success_message.add("target", target)
        return success_message()

@helper.parse_body_request
def train_by_bucket_data(model_id, bucket_id):
    features, target = get_data_by_bucket_id(bucket_id)
    features = features.T
    try:
        result_ml = helper.model_train(model_id, features, target)
    except Exception as err:
        config.logger.error(str(err))
        config.logger.error(traceback.print_exc())
        # err_message = ml_models.result.ErrorResult()
        return {"Error" : err}
    else:
        success_message = ml_models.get_result(model_id)(**result_ml)
        return success_message()

def dummy():
    return {"message": "Are you trying to access Decision Tree Regression"}, 201