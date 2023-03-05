# pythonのバージョンは任意
FROM python:3.8

WORKDIR /usr/src/backend-auth
ENV FLASK_APP=backend-auth

COPY ./backend-auth/requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
