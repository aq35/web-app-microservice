from flask.cli import FlaskGroup
from app import create_app, db, init_app

cli = FlaskGroup(create_app=create_app)


@cli.command()
def init_db():
    init_app(db)


if __name__ == '__main__':
    cli()
