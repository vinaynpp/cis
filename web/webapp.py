from flask import Blueprint, render_template, send_from_directory
import os

web = Blueprint('web', __name__)

@web.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon_io/favicon.ico', mimetype='image/vnd.microsoft.icon')


@web.route('/')
def index():
    return render_template('index.html')