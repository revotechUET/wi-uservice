import pytest

def pytest_addoption(parser):
  parser.addoption('--port', '-P', type=int, action='store', default=5000, help='Port where service is running')

@pytest.fixture
def port(request):
  return request.config.getoption('--port')
