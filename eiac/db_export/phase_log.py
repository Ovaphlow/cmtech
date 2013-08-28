# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '清空phase_log表'
  globalvars.trunc_log()

  print globalvars.get_time(), '添加phase_log数据（黑龙江）'
  insert_data_hlj()

  print globalvars.get_time(), '添加phase_log数据（哈尔滨）'
  insert_data_hrb()

  print globalvars.get_time(), '删除phase_log表无效数据'
  cursor = globalvars.cnx1.cursor()
  sql = 'DELETE FROM phase_b_log WHERE account is NULL'
  cursor.execute(sql)
  globalvars.cnx1.commit()

def insert_data_hlj():
  cursor = globalvars.cnx2.cursor()
  sql = 'SELECT * FROM tbs001_developprojectbasicinfo'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ( 'SELECT * FROM phase_a1 '
            'WHERE XiangMuMingCheng=%s')
    param = (row[0],)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    if cursor.rowcount == 0:
      continue
    elif cursor.rowcount == 1:
      pid = data1[0][0]
    else:
      print globalvars.get_time(), '数据出错！', row[0]
      pid = data1[0][0]
    log_yushouli(row, pid)
    log_shouli(row, pid)
    log_bumen(row, pid)
    log_fuzeren(row, pid)
    log_tacha(row, pid)
    log_huiyi(row, pid)
    log_pinggu(row, pid)
    log_kaoping(row, pid)
    log_shangbao(row, pid)

  globalvars.cnx1.commit()

def insert_data_hrb():
  cursor = globalvars.cnx3.cursor()
  sql = 'SELECT * FROM tbs001_developprojectbasicinfo'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ( 'SELECT * FROM phase_a1 '
            'WHERE XiangMuMingCheng=%s')
    param = (row[0],)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    if cursor.rowcount == 0:
      continue
    elif cursor.rowcount == 1:
      pid = data1[0][0]
    else:
      print globalvars.get_time(), '数据出错！', row[0]
      pid = data1[0][0]
    log_yushouli(row, pid)
    log_shouli(row, pid)
    log_bumen(row, pid)
    log_fuzeren(row, pid)
    log_tacha(row, pid)
    log_huiyi(row, pid)
    log_pinggu(row, pid)
    log_kaoping(row, pid)
    log_shangbao(row, pid)

  globalvars.cnx1.commit()

def log_yushouli(row, id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b_log '
          'VALUES (%s, %s, %s, %s, %s, %s)')
  param = (id, row[119], '', row[62], '0', '预受理')
  cursor.execute(sql, param)
  sql = ( 'INSERT INTO phase_b_log '
          'VALUES (%s, %s, %s, %s, %s, %s)')
  param = (id, row[119], '', row[136], '0', '核定金额')
  cursor.execute(sql, param)

def log_shouli(row, id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b_log '
          'VALUES (%s, %s, %s, %s, %s, %s)')
  param = (id, row[57], '', row[56], '1', '受理')
  cursor.execute(sql, param)

def log_bumen(row, id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b_log '
          'VALUES (%s, %s, %s, %s, %s, %s)')
  param = (id, row[65], '', row[64], '2', '确认')
  cursor.execute(sql, param)

def log_fuzeren(row, id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b_log '
          'VALUES (%s, %s, %s, %s, %s, %s)')
  param = (id, row[70], '', row[68], '3', '确认')
  cursor.execute(sql, param)

def log_tacha(row, id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b_log '
          'VALUES (%s, %s, %s, %s, %s, %s)')
  param = (id, row[78], '', row[77], '4', '确认')
  cursor.execute(sql, param)

def log_huiyi(row, id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b_log '
          'VALUES (%s, %s, %s, %s, %s, %s)')
  param = (id, row[86], '', row[85], '5', '确认')
  cursor.execute(sql, param)

def log_pinggu(row, id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b_log '
          'VALUES (%s, %s, %s, %s, %s, %s)')
  param = (id, row[88], '', row[87], '6', '确认')
  cursor.execute(sql, param)

def log_kaoping(row, id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b_log '
          'VALUES (%s, %s, %s, %s, %s, %s)')
  param = (id, row[95], '', row[94], '7', '确认')
  cursor.execute(sql, param)

def log_shangbao(row, id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b_log '
          'VALUES (%s,%s,%s,%s,%s,%s)')
  param = (id, row[115], '', row[112], '8', '确认')
  cursor.execute(sql, param)
