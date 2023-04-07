FROM revotech2017/wi-python-ml-common:common2

WORKDIR /app
# Setup
ADD setup.py /
ADD dev.config.py /
ADD wsgi.py /
ADD . /app

RUN pip3 install git+https://github.com/KienMN/wi-ml-toolkit

RUN pip3 uninstall keras -y
RUN pip3 install keras==2.3.1

CMD ["python3", "./setup.py","run_server_dev","-P","5001"]
