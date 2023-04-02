import os
from flask import Flask
from flask_mail import Mail

from flask_migrate import Migrate
from api.database import db
import config


migrate = Migrate()
mail = Mail()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'my_secret_key'

    app.config.from_object('config.Config')
    db.init_app(app)

    # ログ設定を行う
    from . import flaskr_logging
    # ログの設定
    log_path = './logs/api.log'
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

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")

    from . import contact
    app.register_blueprint(contact.bp)

    return app


app = create_app()
