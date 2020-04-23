FROM revotech2017/wi-python-ml-common:common3

WORKDIR /app
# Setup
ADD setup.py /
ADD dev.config.py /
ADD wsgi.py /
ADD . /app

CMD ["python3", "./setup.py","run_server_dev","-P","5001"]
