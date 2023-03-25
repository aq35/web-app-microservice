#!/bin/bash
#!chmod +x ./sh/flask.sh
#! ./sh/flask.sh flask

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

