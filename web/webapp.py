from flask import Blueprint, render_template, send_from_directory
import os

web = Blueprint('web', __name__)





@web.route('/')
def index():
    return render_template('index.html')
