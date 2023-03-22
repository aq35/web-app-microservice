#!/bin/bash

#!.envファイルの設定値を参照する
source .env

echo $APP_CONTAINER_NAME"コンテナを操作したい"
echo "1. flaskルートリスト取得"
echo "2. データベースの初期化"
echo "3. ls 実行"
echo "4. アプリ 起動"
read -p "(1,2,3,4)を選択してください。: " choice

case $choice in
  1)
    ./sh/libs/docker-exec.sh $APP_CONTAINER_NAME flask routes
    ;;
  2)
    ./sh/libs/docker-exec.sh $APP_CONTAINER_NAME flask init-db
    ;;
  3)
    ./sh/libs/docker-exec.sh $APP_CONTAINER_NAME ls
    ;; 
  4)
    ./sh/libs/docker-exec.sh $APP_CONTAINER_NAME flask --app flaskr run --debug
    ;;        
  *)
    echo "Invalid choice"
    ;;
esac
