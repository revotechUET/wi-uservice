import requests
import json
import pytest
import sys
from sklearn.datasets import load_breast_cancer
import numpy as np

@pytest.mark.filterwarnings("ignore:DeprecationWarning")
def test_create(port):
  base_url = 'http://127.0.0.1:' + str(port) + '/api'
  model_id = 'test_svm_01'
  body = {
    'model_id': model_id,
    'kernel': 'rbf',
    'degree': 3,
    'C': 1.0,
    'gamma': 0.05,
    'tol': 0.001,
    'max_iter': 10
  }
  
  res = requests.post(base_url + '/model/create/svm',
                      data=json.dumps(body),
                      headers={'Content-Type': 'application/json'})
  print()
  print('Test creating model:')
  print('Resquest:', json.dumps(body))
  print('Response:', res.json())

  assert res.status_code == 201

@pytest.mark.filterwarnings("ignore:DeprecationWarning")
def test_train(port):
  base_url = 'http://127.0.0.1:' + str(port) + '/api'
  model_id = 'test_svm_01'
  X, y = load_breast_cancer(return_X_y=True)
  body = {
    'model_id': model_id,
    #'features': [[1, 1, 2], [2, 1, 3], [1, 2, 3], [1, 2, 2]],
    #'target': [1, 2, 2]
    'features': X.T.tolist(),
    'target': y.tolist()
  }
  res = requests.post(base_url + '/model/train',
                      data=json.dumps(body),
                      headers={'Content-Type': 'application/json'})
  print()
  print('Test training model:')
  print('Resquest:', json.dumps(body))
  print('Response:', res.json())
  assert res.status_code == 201

@pytest.mark.filterwarnings("ignore:DeprecationWarning")
def test_create_bucket_data(port):
  base_url = 'http://127.0.0.1:' + str(port) + '/api'
  bucket_id = 'test_bucket'
  X, y = load_breast_cancer(return_X_y=True)
  body = {
    'bucket_id': bucket_id,
    'dims': X.shape[1] + 1
  }
  res = requests.post(base_url + '/data',
                      data=json.dumps(body),
                      headers={'Content-Type': 'application/json'})
  print()
  print('Test creating bucket data:')
  print('Resquest:', json.dumps(body))
  print('Response:', res.json())
  assert res.status_code == 201

@pytest.mark.filterwarnings("ignore:DeprecationWarning")
def test_push_bucket_data(port):
  base_url = 'http://127.0.0.1:' + str(port) + '/api'
  bucket_id = 'test_bucket'
  X, y = load_breast_cancer(return_X_y=True)
  body = {
    'bucket_id': bucket_id,
    #'data': [[1, 1, 2], [2, 1, 3], [1, 2, 3], [1, 2, 2], [1, 2, 2]]
    'data': np.append(X.T, y.reshape(1, -1), axis = 0).tolist()
  }
  res = requests.put(base_url + '/data',
                     data=json.dumps(body),
                     headers={'Content-Type': 'application/json'})
  print()
  print('Test pushing bucket data:')
  print('Resquest:', json.dumps(body))
  print('Response:', res.json())
  assert res.status_code == 201

@pytest.mark.filterwarnings("ignore:DeprecationWarning")
def test_train_by_bucket_data(port):
  base_url = 'http://127.0.0.1:' + str(port) + '/api'
  model_id = 'test_svm_01'
  bucket_id = 'test_bucket'
  body = {
    'model_id': model_id,
    'bucket_id': bucket_id
  }
  res = requests.post(base_url + '/model/train_by_bucket_data',
                      data=json.dumps(body),
                      headers={'Content-Type': 'application/json'})
  print()
  print('Test training model by bucket data:')
  print('Resquest:', json.dumps(body))
  print('Response:', res.json())
  assert res.status_code == 201

@pytest.mark.filterwarnings("ignore:DeprecationWarning")
def test_predict(port):
  base_url = 'http://127.0.0.1:' + str(port) + '/api'
  model_id = 'test_svm_01'
  X, y = load_breast_cancer(return_X_y=True)
  body = {
    'model_id': model_id,
    #'features': [[1, 1, 2], [2, 1, 3], [1, 2, 3], [1, 2, 2]]
    'features': X.T.tolist()
  }
  res = requests.post(base_url + '/model/predict',
                      data=json.dumps(body),
                      headers={'Content-Type': 'application/json'})
  print()
  print('Test model prediction:')
  print('Resquest:', json.dumps(body))
  print('Response:', res.json())
  assert res.status_code == 201 and len(res.json()['target']) == len(body['features'][0])

@pytest.mark.filterwarnings("ignore:DeprecationWarning")
def test_delete_bucket_data(port):
  base_url = 'http://127.0.0.1:' + str(port) + '/api'
  bucket_id = 'test_bucket'
  body = {
    'bucket_id': bucket_id
  }
  res = requests.delete(base_url + '/data',
                        data=json.dumps(body),
                        headers={'Content-Type': 'application/json'})
  print()
  print('Test deleting bucket data:')
  print('Resquest:', json.dumps(body))
  print('Response:', res.json())
  assert res.status_code == 201
