# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import request

def get():
  template = globalvars.jinja_env.get_template('template/saomiao.html')
  return template.render()

def post():
  s, t = '0', '0'
  if 'female' in request.form.getlist('check'):
    s = '1'
  if 'stow' in request.form.getlist('check'):
    t = '1'
  sql = ( 'INSERT INTO dangan '
          'VALUES('
          '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
  param = ( 0, request.form['aid'], request.form['idcard'],
            request.form['name'], request.form['gender'], request.form['dob'],
            request.form['retiredate'], '', '',
            '', s, t)
  cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
  cursor = cnx.cursor()
  cursor.execute(sql, param)
  cnx.commit()
  template = globalvars.jinja_env.get_template('template/saomiao.html')
  return template.render()
