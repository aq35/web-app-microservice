import click
from flask.cli import with_appcontext
from flaskr.database import db


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)

    author = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __init__(self, author_id, title, body):
        self.author_id = author_id
        self.title = title
        self.body = body

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Post.query.all()

    @staticmethod
    def get_by_id(id):
        return Post.query.filter_by(id=id).first()

    def __repr__(self):
        return '<Post %r>' % self.title
    
    @classmethod
    def create(cls, title, body, author_id):
        post = cls(title=title, body=body, author_id=author_id)
        db.session.add(post)
        db.session.commit()
        return post


def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db.create_all()
    click.echo('Initialized the database.')
