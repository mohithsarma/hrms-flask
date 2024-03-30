from flask import render_template
from flask.blueprints import Blueprint

blueprint = Blueprint('index', __name__)



@blueprint.route('/')
def home():
    """
        set the / to index.html
    """
    return render_template('index.html'), 200
