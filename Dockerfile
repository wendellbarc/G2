FROM ubuntu:14.04
MAINTAINER Wendell Barcellos "wendellbarc@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"] 
CMD ["weather.py"]


