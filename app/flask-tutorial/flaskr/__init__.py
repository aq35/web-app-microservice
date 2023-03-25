import os
from flask import Flask
from flask_mail import Mail

from flask_migrate import Migrate

migrate = Migrate()
mail = Mail()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'my_secret_key'
    # app.config.from_mapping(
    #     SECRET_KEY="dev",
    #     DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    # )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_pre_ping': True,
        'pool_recycle': 3600,
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql/flask-app?charset=utf8mb4'
    app.config.from_mapping(
        # ...
        DB_HOST='mysql',
        DB_USER='root',
        DB_PASSWORD='password',
        DB_NAME='flask-app'
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
    app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
    app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
    app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

    mail.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)
    migrate.init_app(app, db)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")

    from . import contact
    app.register_blueprint(contact.bp)

    return app
