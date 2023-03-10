#!/bin/bash
#!chmod +x dc.sh
#!./dc.sh 
echo "DockerComposeを操作しますか？"
echo "1. まとめてコンテナ起動したい"
echo "2. まとめてコンテナビルドしたい(ビルド時にキャッシュは使用しない)"
read -p "(1,2)を選択してください。: " choice

case $choice in
  1)
    docker-compose up
    ;;
  2)
    docker-compose build --no-cache
    ;;
  *)
    echo "Invalid choice"
    ;;
esac