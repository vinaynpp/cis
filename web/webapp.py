from flask import Blueprint, render_template, send_from_directory, request, redirect, url_for, flash, jsonify
import os
import yara

from werkzeug.utils import secure_filename

from yaraoyara.matchmaking import matchthis

web = Blueprint('web', __name__)
UPLOAD_FOLDER = 'uploaded/'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'exe','ini','conf','html','htm','css','js','json','xml','yara','yml',
                      'sh', '', '*'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@web.route('/')
def index():
    return render_template('index.html')


@web.route('/match', methods=['GET', 'POST'])
def match():
    print(request)
    if request.method == 'GET':
        return render_template('match.html')
    elif request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            print("nofile")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(file)
        if file.filename == '':
            print("nofilename")
            flash('No selected file')
            return redirect(request.url)
        if file :
    #    if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            loadedrules = yara.load('yaraoyara/loaded.bin')
            result = loadedrules.match(filepath)
            os.remove(filepath)
            print(result)
            if not result:
                result.append("CLEAN")

            return redirect(url_for('web.results', tresult=result))
        else:
            render_template('index.html')
            flash("Format not suported")

        return render_template('index.html')


@web.route('/results/<tresult>')
def results(tresult):
    return render_template('results.html', result=tresult)
