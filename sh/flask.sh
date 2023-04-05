#!/bin/bash
#!chmod +x ./sh/flask.sh
#! ./sh/flask.sh flask
#! ./sh/flask.sh pip freeze #現在の環境の設定ファイルを書き出し

#!.envファイルの設定値を参照する
source .env

# コンテナが実行中であることを確認する
RUNNING=$(docker inspect --format="{{.State.Running}}" $APP_CONTAINER_NAME 2> /dev/null)
if [ $? -eq 1 ]; then
  echo "Error: Container $APP_CONTAINER_NAME does not exist." >&2
  exit 1
fi
if [ "$RUNNING" == "false" ]; then
  echo "Error: Container $APP_CONTAINER_NAME is not running." >&2
  exit 1
fi

# 任意の数だけ引数を取得する
ARGS=""
for ARG in "$@"
do
  ARGS="$ARGS $ARG"
done

./sh/libs/docker-exec.sh $APP_CONTAINER_NAME "$ARGS"
# ./sh/flask.sh pip show sqlalchemy
# ./sh/flask.sh pip show sqlalchemy
# ./sh/flask.sh pip list
# pip の　WTFormsがあるか調べる。
# ./sh/flask.sh pip list | grep WTForms
# pip の　WTFormsの詳細情報を調べる。
# ./sh/flask.sh pip show WTForms
# ./sh/flask.sh pip install -r requirements.txt
# ./sh/flask.sh flask db init
# ./sh/flask.sh flask db migrate
# ./sh/flask.sh flask db migrate -m "create_users_table"
