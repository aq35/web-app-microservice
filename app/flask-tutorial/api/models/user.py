from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from typing import Optional
from api.database import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def user_by_user_id(id: int) -> Optional['User']:
        return User.query.filter_by(id=id).first()

    def user_by_username(username: str) -> Optional['User']:
        return User.query.filter_by(username=username).first()
