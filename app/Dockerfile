FROM python:3.8-slim-buster

WORKDIR app

COPY ./flask-tutorial/ ./

RUN pip3 install -r requirements.txt

ENV FLASK_APP=flaskr.__init__
ENV FLASK_ENV=development

CMD ["flask", "init-db"]
# ホストを127.0.0.1にすると、Nigixの可変なIPアドレスに対応できない
# --host=0.0.0.0は、全てのIPを受け入れます。
# * Docker使わない場合は、127.0.0.1を使いましょう。
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
#export FLASK_APP=flaskr
#export FLASK_ENV=development
#flask init-db
#flask run