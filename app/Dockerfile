FROM python:3.8-slim-buster

WORKDIR app

COPY ./flask-tutorial/ ./

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

## python-dotenvによりアプリケーション直下に.envがあればENVを読み込んでくれるようになったため、コメントアウト
## ENV FLASK_APP=api.__init__
## ENV FLASK_DEBUG=development

CMD ["flask", "init-db"]
# ホストを127.0.0.1にすると、Nigixの可変なIPアドレスに対応できない
# --host=0.0.0.0は、全てのIPを受け入れます。
# * Docker使わない場合は、127.0.0.1を使いましょう。
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload", "--debugger"]
#export FLASK_APP=api
#export FLASK_DEBUG=development
#flask init-db
#flask run