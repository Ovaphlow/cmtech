# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
import os
from flask import request, render_template
from werkzeug import secure_filename

def get():
  '''
  template = globalvars.jinja_env.get_template('test.html')
  return template.render()
  '''
  return render_template('test.html')

def post():
  return render_template('test.html')