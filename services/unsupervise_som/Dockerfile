FROM ubuntu:18.04

# Setup
RUN apt-get update
RUN apt-get upgrade -y 
RUN apt-get install -y python3-pip
RUN apt-get install -y python3.7 
ADD setup.py /
ADD dev.config.py /
ADD wsgi.py /
ADD . /

RUN pip3 install numpy scipy connexion[swagger-ui] Flask Flask-Cors gunicorn openapi-spec-validator pylint pymongo PyYAML requests sklearn joblib
RUN apt-get -y install git
RUN pip3 install git+https://github.com/KienMN/Modified-SOM

CMD ["python3", "./setup.py","run_server_dev","-P","5001"]
