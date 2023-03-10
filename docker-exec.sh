#!/bin/bash
#!Dockerコンテナ内に対してコマンドを打つ
#!chmod +x docker-exec.sh
#!./dc.sh <コンテナ名> ./app/flaskapp/linter.py

# コンテナ名を指定
CONTAINER_NAME="$1"
shift
COMMAND="$@"

# コンテナの ID を取得
CONTAINER_ID=$(docker ps -aqf "name=$CONTAINER_NAME")

echo "$CONTAINER_ID"

# コンテナ内でコマンドを実行
docker exec "$CONTAINER_ID" sh -c "$COMMAND"