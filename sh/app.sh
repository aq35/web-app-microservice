#!/bin/bash

#!.envファイルの設定値を参照する
source .env

echo $APP_CONTAINER_NAME"コンテナを操作したい"
echo "1. pyモジュールによる品質向上"
echo "2. コンテナ内のlsコマンド 実行"
read -p "(1,2)を選択してください。: " choice

case $choice in
  1)
    ./scripts/libs/docker-exec.sh $APP_CONTAINER_NAME python3 linter.py
    ;;
  2)
    ./scripts/libs/docker-exec.sh $APP_CONTAINER_NAME ls
    ;;
  *)
    echo "Invalid choice"
    ;;
esac