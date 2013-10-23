# -*- coding=UTF-8 -*-
from flask import request, render_template
from werkzeug import secure_filename
import main
import globalvars
import time
import os


def get():
    return render_template('test.html')


def post():
    #print 'headers', request.headers
    id = request.args.get('id', '')
    #print 'id', id
    #print 'request.value', request.values
    aid = globalvars.get_aid(id)
    fp = '%s\\%s' % (globalvars.G_UPLOAD_PATH, aid)
    globalvars.check_path(fp)
    for f in request.files.getlist('Filedata'):
        if f and globalvars.check_ext(f.filename):
            fn = secure_filename(f.filename)
            fp = os.path.join(fp, fn)
            f.save(fp)
            return '[%s]上传完成'  % (fn)
