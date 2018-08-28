FROM python:alpine
MAINTAINER Wendell Barcellos "wendellbarc@gmail.com"
COPY . /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"] 
CMD ["weather.py"]

