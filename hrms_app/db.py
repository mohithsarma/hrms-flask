from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def init_app(app):
    """
        initialize the database update the changes 
    """
    db.init_app(app)
    migrate.init_app(app, db)


@contextmanager
def transaction():
    try:
        yield
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise


def persist(*args):
    db.session.add_all(args)


def delete(obj):
    db.session.delete(obj)


def execute(sql):
    """
    execute the commands depending on the database  
    """
    return db.session.execute(sql)
