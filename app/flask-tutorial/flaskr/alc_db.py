from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)


def get_engine():
    return db.create_engine(db.engine.url)
