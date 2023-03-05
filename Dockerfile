# pythonのバージョンは任意
FROM python:3.8

WORKDIR /usr/src/backend-outside
ENV FLASK_APP=backend-outside

COPY /backend-outside/requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
