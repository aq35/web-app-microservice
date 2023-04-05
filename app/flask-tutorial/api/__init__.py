import os
from flask import Flask
from flask_mail import Mail

from flask_migrate import Migrate
from api.database import db
import config
from flask_wtf.csrf import generate_csrf

migrate = Migrate()
mail = Mail()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'my_secret_key'
    app.config.from_object(config.Config)
    db.init_app(app)
    app.config.update(config.Config.MAIL)

    # ログ設定を行う
    from . import flaskr_logging
    log_path = './logs/api.log'
    flaskr_logging.log_config(app)
    flaskr_logging.sqlalchemy_logging_config(log_path)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    mail.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .views.auth import auth_router
    app.register_blueprint(auth_router)

    from .views.blog import blog_router
    app.register_blueprint(blog_router)
    app.add_url_rule("/", endpoint="index")

    from .views.contact import contact_router
    app.register_blueprint(contact_router)

    return app


app = create_app()


@app.context_processor
def csrf_context():
    return dict(csrf_token=generate_csrf())
