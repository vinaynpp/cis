from flask import Blueprint, render_template

api = Blueprint('api', __name__)


@api.route('/')
def index():
    return render_template('api/index.html')

