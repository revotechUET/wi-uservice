import numpy as np
import bson
import traceback

from src.config import db
from src.model_helper import parse_body_request
from src import config

try:
    db.create_collection("training_data")
except Exception:
    pass

@parse_body_request
def create(bucket_id, dims):
    try:
        bucket = {"bucket_id": bucket_id, "dims": dims, "data": []}
        col = db["training_data"]
        if col.find_one({"bucket_id": bucket_id}) is not None:
          db.training_data.find_one_and_update(
            {"bucket_id": bucket_id},
            {"$set": {"data": [],"dims" : dims}}
          )
          return {"message": "Bucket data refresh"}, 201
        col.insert_one(bucket)
        #bucket_id = col.insert_one(bucket).inserted_id
    except Exception as err:
        config.logger.error(traceback.print_exc())
        return {"message": str(err)}, 400
    else:
        return {"message": "Create success", "bucket_id": str(bucket_id)}, 201

@parse_body_request
def push(bucket_id, data):
    try:
        arr_check = np.array(data).T
        if not isinstance(arr_check, np.object):
            raise ValueError("Bad data")
        #doc_id = bson.ObjectId(bucket_id)
        #doc = db.training_data.find_one({"_id": doc_id})
        doc = db.training_data.find_one({"bucket_id": bucket_id})
        if doc["dims"] != arr_check.shape[1]:
            raise ValueError("Bad data")
        else:
            doc["data"].extend(arr_check.tolist())
            db.training_data.find_one_and_update({"bucket_id": bucket_id}, {"$set": {"data": doc["data"]}})
            #db.training_data.find_one_and_update({"_id": doc_id}, {"$set": {"data": doc["data"]}})
    except Exception as err:
        config.logger.error(traceback.print_exc())
        return {"message": str(err)}, 400
    else:
        return {"message": "Push data success"}, 201

@parse_body_request
def delete(bucket_id):
    try:
        #doc_id = bson.ObjectId(bucket_id)
        #db["training_data"].find_one_and_delete({"_id": doc_id})
        db.training_data.find_one_and_delete({"bucket_id": bucket_id})
    except Exception as err:
        config.logger.error(traceback.print_exc())
        return {"message": str(err)}, 400
    else:
        return {"message": "Delete success"}, 201

@parse_body_request
def get_data_by_bucket_id(bucket_id):
    try:
        doc = db.training_data.find_one({'bucket_id': bucket_id})
        data = np.array(doc['data'])
        features = data[:, :-1].T
        target = data[:, -1]
    except Exception as err:
        config.logger.error(traceback.print_exc())
        return None, None
    else:
        return features, target

def get_all_buckets():
    try: 
        buckets = db.training_data.distinct("bucket_id")
        trim = db.training_data.distinct("dim")
        to_return = []
        for i in range(0, len(buckets)):
            tmp = []
            tmp.append(buckets[i])
            tmp.append(dim[i])
            to_return.append(tmp)
    except Exception as err:
        config.logger.error(traceback.print_exc())
        return None
    else:
        return to_return
