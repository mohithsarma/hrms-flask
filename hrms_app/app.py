from flask import Flask
from . import db
from . import settings
from .blueprints import index, employee


def create_app():
    """
        Create Flask app and initialize the database. 
    """
    app = Flask(__name__)
    settings.init_app(app)
    db.init_app(app)

    app.register_blueprint(index.blueprint)
    app.register_blueprint(employee.blueprint, url_prefix='/employee')

    return app
