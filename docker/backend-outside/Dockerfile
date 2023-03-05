# pythonのバージョンは任意
FROM python:3.8

WORKDIR /usr/src/app
ENV FLASK_APP=backend-outside

COPY /backend-outside/requirements.txt ./app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
