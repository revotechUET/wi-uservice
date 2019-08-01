# Base Rest API for  Service.
Python server for ML model using Flask framework and Gunicorn WSGI server.

## Prerequisite
Required package can be found in requirement.txt.  
Besides, `wi_ml_toolkit` package are available in `wi-ml-toolkit` repo on Github.

## Structure
```bash
├── README.md                 // this file
├── dev.config.py             // configuration of Gunicorn WSGI for development deployment
├── prod.config.py            // configuration of Gunicorn WSGI for product deployment
├── requirements.txt          // required packages
├── setup.py                  // information for installation and commands
├── src                       // source code of the service
│   ├── __init__.py           // connexion application definition 
│   ├── config.py
│   ├── controllers           // operations to handle requests
│   │   ├── __init__.py
│   │   ├── create.py
│   │   └── data.py
│   ├── ml_models             // data models and machine learning models
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── huber.py                // estimator, result and validator models
│   │   │   └── huber_estimator.py      // machine learning model class
│   │   ├── result.py
│   │   └── validator.py
│   ├── model_helper.py       // general operations of machine learning model
│   ├── specs
│   │   └── openapi.yaml      // open API specification
│   └── tests
│       ├── conftest.py       // addition options for pytest
│       └── test_requests.py  // test cases for testing requests
├── static                    // folder to save machine learning instances
└── wsgi.py                   // import connextion app from src directory
```

## Database configuration
Configuration for the service to use MongoDB when start container. Configuration can be found in `config.py` files.
* DB_HOST
* DB_PORT
* DB_NAME
* DB_USER
* DB_PASS

## OpenAPI Specification
Source: `src/specs/openapi.yaml`  
Defination of all API of the service.  
Read more about OpenAPI Specification v2 and v3 at <https://swagger.io/specification/>

## Machine learning model
Source: `src/ml_models/models/huber_estimator.py`  
Machine learning model class. The class should be compatible with sklearn.pipeline.Pipeline class and implemented fit and predict method. It should be named as `WiEstimator` to be able to be imported from other files.

## Machine learning pipeline
Source: `src/ml_models/__init__.py`  
Method: build_model  
Preprocessing and machine learning model classes are used in a Pipeline. Editing components in Pipeline to make your own Pipeline.

## Result of training
Source: `src/model_helper.py`  
Method: model_train   
`result` parameter is used as a dict to store metrics of training process. Editing key-value pair in `result` to return your own metrics corresponding to your training.

## Addition operations
Source: `src/controllers`  
Addition operations to handle requests should be written in `controller` folder.

## Setup file
Source: `setup.py`  
This file contains information for installation and commands. Information is passed as parameters in setup function of `setuptools` package. Commands are defined as subclasses of `distutils.command.sdist.sdist`.

## Starting service
Service can be started by direct command
```bash
gunicorn -c dev.config.py wsgi:application -b :5000
```
or via setup.py
```bash
python3 setup.py run_server_dev -P 5000
```

## Test
Test cases are written in `src/tests` folder. Running test cases by command
```bash
pytest src/test/test_requests.py -v -s -P 5000
```
or via setup.py
```bash
python3 setup.py run_test_requests -P 5000
```

## References
Connexion: <https://connexion.readthedocs.io/en/latest/>  
Gunicorn: <http://docs.gunicorn.org/en/stable/>  
OpenAPI Specification: <https://swagger.io/specification/>  
Pytest: <https://docs.pytest.org/en/latest/>  
Python-packaging: <https://python-packaging.readthedocs.io/en/latest/>  
Python setup.py to run shell script: <https://stackoverflow.com/questions/17887905/python-setup-py-to-run-shell-script/>  
Add custom commands to setup.py: <https://jichu4n.com/posts/how-to-add-custom-build-steps-and-commands-to-setuppy/>
