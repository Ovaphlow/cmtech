# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '修正A1表环评类别'
  update_a1_hplb()
  print globalvars.get_time(), '修正A1表环统类别'
  update_a1_htlb()

def update_a1_hplb():
  cursor = globalvars.cnx1.cursor()
  sql = 'SELECT * FROM phase_a1'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor_origin = globalvars.cnx2.cursor()

  for row in data:
    sql = ( 'SELECT * FROM tbs001_basicdatasub '
            'WHERE id=%s')
    param = (row[17],)
    cursor_origin.execute(sql, param)
    data_origin = cursor_origin.fetchall()

    if cursor_origin.rowcount > 0:
      sql = ( 'UPDATE phase_a1 '
              'SET '
              'HuanPingLeiBie=%s '
              'WHERE id=%s')
      param = (data_origin[0][2], row[0])
      cursor.execute(sql, param)

  globalvars.cnx1.commit()

def update_a1_htlb():
  sql = 'SELECT * FROM phase_a1'
  cursor = globalvars.cnx1.cursor()
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor_origin = globalvars.cnx2.cursor()

  for row in data:
    sql = ( 'SELECT * FROM tbs001_basicdatasub '
            'WHERE id=%s')
    param = (row[18],)
    cursor_origin.execute(sql, param)
    data_origin = cursor_origin.fetchall()

    if cursor_origin.rowcount > 0:
      sql = ( 'UPDATE phase_a1 '
              'SET '
              'HuanTongLeiBie=%s '
              'WHERE id=%s')
      param = (data_origin[0][2], row[0])
      cursor.execute(sql, param)

  globalvars.cnx1.commit()

if __name__ == '__main__':
  run()
