# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import request
from werkzeug import secure_filename
def get():
  template = globalvars.jinja_env.get_template('template/saomiao.html')
  return template.render()

def post():
  f = request.files['file']
  filename = secure_filename(f.filename)
  print filename
  template = globalvars.jinja_env.get_template('template/saomiao.html')
  return template.render()

