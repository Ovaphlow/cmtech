# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '清空phase_a4表'
  globalvars.trunc_a4()

  print globalvars.get_time(), '添加phase_a4数据（黑龙江）'
  insert_data_hlj()

  print globalvars.get_time(), '添加phase_a4数据（哈尔滨）'
  insert_data_hrb()

def insert_data_hlj():
  cursor = globalvars.cnx2.cursor()
  sql = ( 'SELECT * '
          'FROM tbs001_huanjing '
          'ORDER BY id')
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ( 'SELECT * '
            'FROM phase_a1 '
            'WHERE XiangMuMingCheng=%s')
    param = (row[1],)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    if cursor.rowcount == 0:
      continue
    else:
      pid = data1[0][0]
      sql = 'SELECT COUNT(*) FROM phase_a4 WHERE id=%s'
      param = (pid,)
      cursor.execute(sql, param)
      row1 = cursor.fetchone()
      if row1[0] == 0:
        sql = ( 'INSERT INTO phase_a4 '
                'VALUES (%s, %s, %s, %s, %s, %s,'
                '%s, %s, %s, %s, %s, %s,'
                '%s, %s, %s, %s, %s, %s)')
        param = ( pid, row[2], row[3], row[4], row[5], row[6],
                  row[7], row[8], row[9], row[10], row[11], row[12],
                  row[13], row[14], row[15], row[16], row[17], row[18],)
        cursor.execute(sql, param)
      else:
        pass

  globalvars.cnx1.commit()

def insert_data_hrb():
  cursor = globalvars.cnx3.cursor()
  sql = ( 'SELECT * '
          'FROM tbs001_huanjing '
          'ORDER BY id')
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ( 'SELECT * '
            'FROM phase_a1 '
            'WHERE XiangMuMingCheng=%s')
    param = (row[1],)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    if cursor.rowcount == 0:
      continue
    else:
      pid = data1[0][0]
      sql = 'SELECT COUNT(*) FROM phase_a4 WHERE id=%s'
      param = (pid,)
      cursor.execute(sql, param)
      row1 = cursor.fetchone()
      if row1[0] == 0:
        sql = ( 'INSERT INTO phase_a4 '
                'VALUES (%s, %s, %s, %s, %s, %s,'
                '%s, %s, %s, %s, %s, %s,'
                '%s, %s, %s, %s, %s, %s)')
        param = ( pid, row[2], row[3], row[4], row[5], row[6],
                  row[7], row[8], row[9], row[10], row[11], row[12],
                  row[13], row[14], row[15], row[16], row[17], row[18],)
        cursor.execute(sql, param)
      else:
        pass

  globalvars.cnx1.commit()
