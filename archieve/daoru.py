# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
import os
from werkzeug import secure_filename
from flask import request
import xlrd

def get():
  template = globalvars.jinja_env.get_template('template/daoru.html')
  return template.render()

def post():
  f = request.files['file']
  filename = secure_filename(f.filename)
  file_path = os.path.join(globalvars.G_UPLOAD_PATH, filename)
  f.save(file_path)
  import_xls(file_path)
  template = globalvars.jinja_env.get_template('template/daoru.html')
  return template.render()

def import_xls(file_path):
  print file_path
  xls = xlrd.open_workbook(file_path, 'rb')
  sh = xls.sheets()[0]
  print sh.name
  cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
  cursor = cnx.cursor()
  for row in range(1, sh.nrows):
    sql = ( 'INSERT INTO dangan '
            'VALUES('
            '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
    param = ( 0, sh.cell(row, 3).value, sh.cell(row, 0).value,
              sh.cell(row, 1).value, sh.cell(row, 2).value, '',
              '', sh.cell(row, 4).value, sh.cell(row, 5).value,
              sh.cell(row, 6).value, 0, 0)
    cursor.execute(sql, param)
  cnx.commit()
