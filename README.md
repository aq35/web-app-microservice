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

## Flaskアプリケーションが正常に起動しているかどうかを確認するために、次のコマンドを実行してください。
docker-compose logs myapp
以下ならOK
myapp_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

upstream設定が正しいかどうか
location設定が正しいかどうか

## Nginxのログを確認して、どのような問題があるかを確認することができます。次のコマンドを実行して、Nginxのログを確認してください。
docker-compose logs myapp-nginx

docker-compose logs myapp-nginx の出力結果を見る限り、nginxのコンテナは起動しているようです。そのため、問題はFlaskのコンテナにある可能性が高いです。

Flaskが起動している場合は、次にnginxの設定を確認してください。
docker-compose.yml ファイルで定義した myapp-nginx コンテナの設定ファイル nginx.conf に、Flaskアプリケーションへのアクセスが適切に設定されていることを確認してください。
特に、upstream ディレクティブと location ディレクティブについて、正しく設定されているかどうかを確認してください。

docker-compose exec myapp-nginx /bin/bash
cat /etc/nginx/nginx.conf
upstreamディレクティブが正しく設定されていることを確認します。以下のような行があるはずです。
upstream app_server {
    server myapp:5000;
}
locationディレクティブが正しく設定されていることを確認します。以下のような行があるはずです。
location / {
    proxy_pass http://app_server;
}

設定ファイルを保存してNginxを再起動します。
service nginx restart

502 Bad Gateway エラーが発生するのは、NginxがupstreamのFlaskアプリケーションに接続できなかった場合です。アプリケーションがコンテナ内でcurlできたことから、Nginxの設定に問題があると考えられます。以下のことを確認してみてください。

1.NginxコンテナとFlaskコンテナが同じネットワークに所属していることを確認してください。
networks:
  my_network:
2.Flaskアプリケーションのポート番号が5000番であることを確認してください。
    ports:
      - "5000:5000"
3.Nginxの設定ファイルで、upstreamで指定するFlaskアプリケーションの名前が、Docker Composeファイルで定義されているサービス名と一致していることを確認してください。

Docker Composeファイルを開き、Flaskアプリケーションのサービス名を確認します。例えば、以下のような設定の場合、サービス名は「myapp」となります。
services:
  myapp:
    build: ./app

upstream myapp {
    server myapp:5000;
}

server {
    listen 80;
    server_name localhost;
    
    location / {
        proxy_pass http://myapp;
    }
}
4.Nginxの設定ファイルで、locationで指定するURLパスが、Flaskアプリケーションで処理するURLパスと一致していることを確認してください。
5.Nginxコンテナのログを確認して、何らかのエラーメッセージがあるかどうか確認してください。
