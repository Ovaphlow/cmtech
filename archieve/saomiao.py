# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import request

def get():
  template = globalvars.jinja_env.get_template('template/saomiao.html')
  return template.render()

def post():
  pass
