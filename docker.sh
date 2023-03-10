#!/bin/bash
# Dockerコンテナ内に対してコマンドを打つ
# chmod +x my_shell.sh
# 以下を実行すると、整形コマンドになる
# ./docker.sh web-app_app black app.py
# ./docker.sh web-app_app flake8 app.py
docker exec $(docker ps -aqf "name=$1") ${@:2}