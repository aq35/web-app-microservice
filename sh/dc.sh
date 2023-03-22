#!/bin/bash
#!chmod +x dc.sh
#!./dc.sh 
echo "DockerComposeを操作しますか？"
echo "1. まとめてコンテナ起動したい"
echo "2. まとめてコンテナビルドしたい(ビルド時にキャッシュは使用しない)"
echo "3. コンテナリストを表示してビルドしたいコンテナを選択する"
read -p "(1,2,3)を選択してください。: " choice

case $choice in
  1)
    docker-compose up
    ;;
  2)
    docker-compose build --no-cache
    ;;
  3)
    containers=$(docker-compose ps --services)
    select container in $containers; do
      if [ -n "$container" ]; then
        docker-compose build --no-cache $container
        break
      fi
    done
    ;;
  *)
    echo "Invalid choice"
    ;;
esac