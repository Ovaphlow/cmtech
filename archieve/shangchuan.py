# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
import os
from flask import request
from werkzeug import secure_filename

def get():
  template = globalvars.jinja_env.get_template('template/shangchuan.html')
  return template.render()

def post():
  files_list = request.files.getlist('file')
  for f in files_list:
    if f and globalvars.check_ext(f.filename):
      filename = secure_filename(f.filename)
      f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
  template = globalvars.jinja_env.get_template('template/shangchuan.html')
  return template.render()
