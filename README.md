## マイクロサービスを開発します。

構成:Python(Flask)+Vue3(Vite)<br>
$ docker-compose down && docker-compose build && docker-compose up -d<br>
$ docker-compose build --no-cache

## フロントエンド (Vue+Vite)のセットアップ
$ cd frontend<br>
$ npm install<br>
$ npm run dev<br>

### バックエンド(側アプリ) (Python+Flask)

### バックエンド+REST API(認証系) (Python+Flask)

### Docker,Docker-Compose
複数のシェルスクリプトを一度に全て有効にする
$ chmod +x *.sh

./dc.sh 対話式Docker-Compose操作
./docker.sh Dockerコンテナ内