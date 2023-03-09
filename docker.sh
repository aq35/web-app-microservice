#!/bin/bash
# Dockerコンテナ内に対してコマンドを打つ
# chmod +x my_shell.sh

docker exec $(docker ps -aqf "name=$1") ${@:2}