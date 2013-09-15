# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
import os
from flask import request, render_template
from werkzeug import secure_filename

def get(id):

  return render_template('shangchuan.boot.html', id=id)

def post(id):
  files_list = request.files.getlist('file')
  for f in files_list:
    if f and globalvars.check_ext(f.filename):
      filename = secure_filename(f.filename)
      f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
  return render_template('shangchuan.boot.html')
