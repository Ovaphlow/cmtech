# -*- coding=UTF-8 -*-

from flask import request, render_template
from werkzeug import secure_filename

def get():
    return render_template('test.html')

def post():
    return render_template('test.html')
