FROM revotech2017/wi-python-ml-common:common1

WORKDIR /app
# Setup
ADD setup.py /
ADD dev.config.py /
ADD wsgi.py /
ADD . /app

RUN pip3 install git+https://github.com/KienMN/Modified-SOM

CMD ["python3", "./setup.py","run_server_dev","-P","5001"]
