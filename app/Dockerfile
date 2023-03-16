FROM python:3.8-slim-buster

WORKDIR app
ENV FLASK_APP=app

COPY ./flask-tutorial/ ./

RUN pip3 install -r requirements.txt

# CMD ["python3", "app.py"]
CMD ["flask", "run", "flaskr",]