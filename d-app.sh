#!/bin/bash

#!.envファイルの設定値を参照する
source .env

echo $APP_CONTAINER_NAME"コンテナを操作したい"
echo "1. linter.py 実行"
echo "2. app内 ls 実行"
read -p "(1,2)を選択してください。: " choice

case $choice in
  1)
    ./docker-exec.sh $APP_CONTAINER_NAME python ./flaskapp/linter.py
    ;;
  2)
    ./docker-exec.sh $APP_CONTAINER_NAME ls
    ;;
  *)
    echo "Invalid choice"
    ;;
esac