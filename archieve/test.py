# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
import os
from flask import request
from werkzeug import secure_filename

def get():
  template = globalvars.jinja_env.get_template('template/test.html')
  return template.render()

def post():
  template = globalvars.jinja_env.get_template('template/test.html')
  return template.render()
