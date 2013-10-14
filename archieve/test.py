# -*- coding=UTF-8 -*-

from flask import request, render_template
from werkzeug import secure_filename
import main

def get():
    return render_template('test.html')

def post():
    with main.app.test_request_context('/test', method='POST'):
        print 'updata:', request.files['updata']