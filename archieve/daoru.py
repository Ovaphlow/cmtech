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
  xls = xlrd.open_workbook(file_path, 'rb')
  sh = xls.sheets()[0]
  cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
  cursor = cnx.cursor()
  for row in range(1, sh.nrows):
    if sh.cell(row, 6).value != u'已调入':
      continue
    sql = 'SELECT id FROM dangan WHERE DangAnHao=%s'
    param = (sh.cell(row, 3).value,)
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if cursor.rowcount == 0:
      sql = ( 'INSERT INTO dangan '
              'VALUES('
              '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
      param = ( 0, sh.cell(row, 3).value, sh.cell(row, 0).value,
                sh.cell(row, 1).value, sh.cell(row, 2).value, '',
                '', sh.cell(row, 4).value, sh.cell(row, 5).value,
                sh.cell(row, 6).value, 0, 0)
      cursor.execute(sql, param)
    else:
      sql = ( 'UPDATE dangan '
              'SET '
              'DangAnHao=%s, ShenFenZheng=%s, XingMing=%s,'
              'XingBie=%s, RenYuanLeiBie=%s, CunDangRiQi=%s,'
              'CunDangZhuangTai=%s '
              'WHERE id=%s')
      param = ( sh.cell(row, 3).value, sh.cell(row, 0).value,
                sh.cell(row, 1).value, sh.cell(row, 2).value,
                sh.cell(row, 4).value, sh.cell(row, 5).value,
                sh.cell(row, 6).value, data[0][0])
      cursor.execute(sql, param)

  cnx.commit()
