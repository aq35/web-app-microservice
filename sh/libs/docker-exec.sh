#!/bin/bash
#!Dockerコンテナ内に対してコマンドを打つ
#!chmod +x docker-exec.sh
#!./docker-exec.sh <コンテナ名> python3 linter.py
#./docker-exec.sh my-app python3 linter.py
# コンテナ名を指定
CONTAINER_NAME="$1"

# コンテナの ID を取得
CONTAINER_ID=$(docker ps -aqf "name=$CONTAINER_NAME")

# コンテナ内でコマンドを実行
docker exec "$CONTAINER_ID" ${@:2}