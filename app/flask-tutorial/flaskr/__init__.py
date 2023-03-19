import os

from flask import Flask


def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)
    # TODO flask-sqlalchemy,flask-migrateを利用する
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )   

    if test_config is None:
        # もしインスタンスフォルダにconfig.pyファイルがあれば、
        # 値をそこから取り出して、標準設定を上書きします。
        # 例えば、デプロイの時には、本当のSECRET_KEYを設定するために使用できます。
        app.config.from_pyfile('config.py', silent=True)
    else:
        # appが使用する標準設定をいくつか設定します。
        app.config.from_mapping(test_config)

    # Flaskはインスタンスフォルダを自動的には作成しませんが、
    # このプロジェクトではそこにSQLiteデータベースファイルを作成するために
    # インスタンスフォルダが作成されている必要があります。
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app