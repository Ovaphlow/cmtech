# -*- coding=UTF-8 -*-

import globalvars
from flask import request, render_template, redirect
from werkzeug import secure_filename

def get(id):
    fp = globalvars.get_file_path(id)
    return render_template('saomiao.html', path=id, filepath=fp)

def post(id):
    return redirect('/shangchuan/%s' % (id))
