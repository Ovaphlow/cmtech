# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import request, redirect

def get(id):
  sql = 'SELECT * FROM dangan WHERE id=%s'
  param = (id,)
  cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
  cursor = cnx.cursor()
  cursor.execute(sql, param)
  data = cursor.fetchall()
  template_param = {
    'row': data[0]
  }
  template = globalvars.jinja_env.get_template('template/dangan.boot.html')
  return template.render(template_param)
