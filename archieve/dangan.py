# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import request, redirect

def get():
  sql = 'SELECT * FROM dangan WHERE id=%d'
  param = (request.args.get('id', ''),)
  cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
  cursor = cnx.cursor()
  cursor.execute(sql)
  data = cursor.fetchall()
  template_param = {
    'row': data[0]
  }
  template = globalvars.jinja_env.get_template('template/dangan_main.html')
  return template.render(template_param)
