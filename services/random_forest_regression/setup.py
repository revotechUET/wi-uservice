from distutils.command.sdist import sdist
from distutils.errors import DistutilsExecError

from setuptools import setup, find_packages

class RunTestRequests(sdist):
  """Command class to run test requests."""
  
  description = 'Running test requests'
  user_options = sdist.user_options + [
    ('port=', 'P', 'Specify the port for running service [default: 5000]')
  ]

  def initialize_options(self):
    sdist.initialize_options(self)
    self.port = None

  def finalize_options(self):
    sdist.finalize_options(self)
    if self.port is None:
      self.port = 5000

  def run(self):
    try:
      self.spawn(['pytest', 'src/tests/test_requests.py', '-v', '-s', '-P', str(self.port)])
    except DistutilsExecError:
      self.warn('Running test requests failed!')

class RunServerDev(sdist):
  """Command class to run server in development mode."""
  
  description = 'Running development server'
  user_options = sdist.user_options + [
    ('port=', 'P', 'Specify the port for running service [default: 5000]')
  ]

  def initialize_options(self):
    sdist.initialize_options(self)
    self.port = None

  def finalize_options(self):
    sdist.finalize_options(self)
    if self.port is None:
      self.port = 5000

  def run(self):
    try:
      self.spawn(['gunicorn', '-c', 'dev.config.py', 'wsgi:application', '-b', ':' + str(self.port)])
    except DistutilsExecError:
      self.warn('Running development server failed!')

class RunServerProd(sdist):
  """Command class to run server in production mode."""
  
  description = 'Running production server'
  user_options = sdist.user_options + [
    ('port=', 'P', 'Specify the port for running service [default: 5000]')
  ]

  def initialize_options(self):
    sdist.initialize_options(self)
    self.port = None

  def finalize_options(self):
    sdist.finalize_options(self)
    if self.port is None:
      self.port = 5000
  def run(self):
    try:
      self.spawn(['gunicorn', '-c', 'prod.config.py', 'wsgi:application', '-b', ':' + str(self.port)])
    except DistutilsExecError:
      self.warn('Running production server failed!')

NAME = "random_forest"
VERSION = '1.0.0'

REQUIRES = [
  "connexion==2.0.0",
  "swagger-ui-bundle==0.0.2"
]

setup(
  name=NAME,
  version=VERSION,
  author_email="info@i2g.cloud",
  url="https://github.com/tunghoang/wi-uservices",
  install_requires=REQUIRES,
  packages=find_packages(),
  package_data={'': ['src/specs/openapi.yaml']},
  include_package_data=True,
  cmdclass={
    'run_test_requests': RunTestRequests,
    'run_server_dev': RunServerDev,
    'run_server_prod': RunServerProd
  }
)
