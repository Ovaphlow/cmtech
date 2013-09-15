# -*- coding=UTF-8 -*-

import globalvars
import mysql.connector
from flask import request, render_template
from werkzeug import secure_filename

def get():
  return render_template('saomiao.html')

def post():
  f = request.files['file']
  filename = secure_filename(f.filename)
  print filename
  return render_template('saomiao.html')