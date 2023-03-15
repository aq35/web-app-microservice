FROM python:3.9.7

WORKDIR /app
ENV FLASK_APP=app

COPY ./flask-tutorial/requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]