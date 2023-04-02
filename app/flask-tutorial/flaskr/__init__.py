import os
from flask import Flask
from flask_mail import Mail

from flask_migrate import Migrate

migrate = Migrate()
mail = Mail()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'my_secret_key'

    app.config.update(
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:password@mysql/flask-app?charset=utf8mb4',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ENGINE_OPTIONS={
            'pool_pre_ping': True,
            'pool_recycle': 3600,
        },
        DB_HOST='mysql',
        DB_USER='root',
        DB_PASSWORD='password',
        DB_NAME='flask-app',
    )

    # ログ設定を行う
    from . import flaskr_logging
    # ログの設定
    log_path = './logs/flaskr.log'
    flaskr_logging.log_config(app)
    flaskr_logging.sqlalchemy_logging_config(log_path)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    app.config.update({
        "MAIL_SERVER": os.environ.get("MAIL_SERVER"),
        "MAIL_PORT": os.environ.get("MAIL_PORT"),
        "MAIL_USE_TLS": os.environ.get("MAIL_USE_TLS"),
        "MAIL_USERNAME": os.environ.get("MAIL_USERNAME"),
        "MAIL_PASSWORD": os.environ.get("MAIL_PASSWORD"),
        "MAIL_DEFAULT_SENDER": os.environ.get("MAIL_DEFAULT_SENDER"),
    })

    mail.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # models.pyをFlaskアプリケーションに登録
    from . import models
    models.init_app(app)
    migrate.init_app(app, models)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")

    from . import contact
    app.register_blueprint(contact.bp)

    return app


app = create_app()
