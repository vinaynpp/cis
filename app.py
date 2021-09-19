from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
import os
from api.apiapp import api
from web.webapp import web
import yara
from git import Repo
from pathlib import Path
import shutil

app = Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(web, static_folder='static', template_folder='templates')
app.register_blueprint(api, url_prefix='/api', static_folder='static', template_folder='templates')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

UPLOAD_FOLDER = '../uploaded/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def initialization():
    dirpath = Path('yaraoyara/repo/')

    if not dirpath.exists():
        Repo.clone_from("https://github.com/Yara-Rules/rules", "yaraoyara/repo/")

    indexdicti = {'malware': 'yaraoyara/repo/malware_index.yar',
        'maldocs': 'yaraoyara/repo/maldocs_index.yar',
        'mobile_malware': 'yaraoyara/repo/mobile_malware_index.yar'}
    rules = yara.compile(filepaths=indexdicti)
    rules.save('yaraoyara/loaded.bin')
    print("ohh it's working")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon_io/favicon.ico', mimetype='image/vnd.microsoft.icon')


app.before_first_request(initialization)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(threaded=True, port=port, debug=True, host="0.0.0.0")
