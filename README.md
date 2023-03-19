## サーバーレス,マイクロサービス,デスクトップアプリ,Docker環境

Python[FW:Flask] を通して、WEBでもデスクトップアプリにでも応用できるコード資産を作っていくことが目的です。

Pythonは、PHPと比べて「WEBアプリの機能実装」において、充実さが劣っている気がします。

それは、PHPは、WEBアプリを作ることに時間をかけてきたからだと思います。

でも、Pythonは、「WEBアプリの機能実装を支える力」がPHPよりも優れていると思います (今のところは)。

「WEBアプリの機能実装を支える力」って一体なんでしょうね。自分でもよくわかりませんが。

例えば、本屋さんにいくと、Pythonの方が書籍が多い印象ですね。

Pythonって開発分野も色々ありますね。

WEB開発だけでなく、ゲーム開発だったり、データ分析だったり、非エンジニアの業務改善用の開発とかとか。

ゲーム開発者が、Pythonユーザーだと、Pythonの書籍を出してくれるかも。そこには、ゲームの面白さを表現する

ノウハウがあるかも。

データ分析者の知見に触れられたら、WEB開発の効率化ももう少し、サイエンスチックになる気がします。

非エンジニア用の業務改善ツールとか、楽しそうですよね。

これらの要素が、最終的に私が目指す「高速開発」の域に近づけるのではないかと思っています。

## Authors

- [@aq35](https://www.github.com/aq35)


## Installation

Docker(nginx+Flask)で開発環境を構築する

```bash
chmod +x ./sh/dc.sh
./sh/dc.sh

Dockerデスクトップを起動したのち、
2 → 1 の順番で実行してください。
echo "1. まとめてコンテナ起動したい"
echo "2. まとめてコンテナビルドしたい(ビルド時にキャッシュは使用しない)"

```
http://localhost/




    
## FAQ

### 502 Bad Gateway エラー が起きた場合

カスタマイズしようとして、502 Bad Gateway エラーになった場合、修正漏れがあるのかもしれません。

nginxやdocker-compose.ymlに少しずつ慣れていきましょう。

#### Flaskアプリケーションが正常に起動しているかどうか

```bash
docker-compose logs myapp
以下ならOK
myapp_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

#### nginx.confは、正しくセットされているか？

docker-compose.yml ファイルで定義した myapp-nginx コンテナの設定ファイル nginx.conf に、Flaskアプリケーションへのアクセスが適切に設定されていることを確認してください。

特に、upstream ディレクティブと location ディレクティブについて、正しく設定されているかどうかを確認してください。
```bash
upstreamディレクティブが正しく設定されていることを確認します。以下のような行があるはずです。
upstream app_server {
    server myapp:5000;
}
locationディレクティブが正しく設定されていることを確認します。以下のような行があるはずです。
location / {
    proxy_pass http://app_server;
}

＊　server myapp:5000;は、docker-compose.ymlの「myapp」です。
docker-compose.yml
services:
  myapp:
    build: ./app
    container_name: ${APP_CONTAINER_NAME}
```


#### ログを見てみよう

nginxのログ

```bash
docker-compose exec myapp-nginx /bin/bash
ls /var/log/nginx/
access.log
error.log

or

./web-app/nginx/log
access.log
error.log
```

flaskのログ

```bash
docker-compose logs myapp
```

#### flaskアプリ Dockerfileを見てみよう

```bash
web-app/app/Dockerfile

ここから
FROM python:3.8-slim-buster

WORKDIR app

COPY ./flask-tutorial/ ./

RUN pip3 install -r requirements.txt

ENV FLASK_APP=flaskr.__init__
ENV FLASK_ENV=development

CMD ["flask", "init-db"]
# ホストを127.0.0.1にすると、Nigixの可変なIPアドレスに対応できない
# --host=0.0.0.0は、全てのIPを受け入れます。
# * Docker使わない場合は、127.0.0.1を使いましょう。
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
#export FLASK_APP=flaskr
#export FLASK_ENV=development
#flask init-db
#flask run

ここまで

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
が
CMD ["flask", "run"]の場合、
127.0.0.1がflaskアプリサーバーのポートに割り当てられる

nginx.confのproxy_passは、127.0.0.1とは限らない。
proxy_pass http://app_server;
なので、flask側も"--host=0.0.0.0"をつけることで、IPを全許可にする。
* コンテナ自体がIPフィルターしているため、アプリはIPフィルターを考えなくて良い。

```

