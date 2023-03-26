import mysql.connector
import click
from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# このプログラムは、Flaskアプリケーションにおいて、データベース接続を行い、
# データベースの初期化や接続のクローズを行うためのユーティリティ関数群を定義しています。


# MySQLデータベースへの接続や切断を行うためのメソッドを提供しています。

class YourDBConnector:
    # データベースへの接続に必要な情報を受け取ります。
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None

    # connectメソッドでは、mysql.connectorモジュールを使用して実際に接続を行っています。
    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.conn

    # 接続を切断するための処理を行っています。
    def close(self):
        if self.conn:
            self.conn.close()

    def init_db(self, conn, schema_file):
        cursor = conn.cursor()
        for statement in schema_file.read().decode('utf8').split(';'):
            cursor.execute(statement)
        cursor.close()
        conn.commit()


# Flaskアプリケーションのコンテキスト内で唯一のデータベース接続オブジェクトを取得するための関数
# gオブジェクトを使用して、コンテキスト内で同じ接続オブジェクトを再利用できるようにしています。
def connect_db():
    if 'db' not in g:
        g.db = get_db_connector().connect()
    return g.db


def get_db_connector():
    if 'db_connector' not in g:
        g.db_connector = YourDBConnector(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_NAME']
        )
    return g.db_connector


# connect_db関数を呼び出して、唯一のデータベース接続オブジェクトを取得するための関数
def get_db():
    if 'db' not in g:
        g.db = connect_db()
    return g.db


# Flaskアプリケーションのコンテキストが終了した際に、データベース接続をクローズするための関数
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        get_db_connector().close()


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


# データベースの初期化を行うための関数
def init_db():
    db_connector = get_db_connector()
    conn = db_connector.connect()
    with current_app.open_resource('schema.sql') as f:
        db_connector.init_db(conn, f)
    conn.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
