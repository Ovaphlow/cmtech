# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '清空pinggu_xiangmufuzeren表'
  globalvars.trunc_xmfzr()

  print globalvars.get_time(), '添加pinggu_xiangmufuzeren数据（黑龙江）'
  insert_data_hlj()

  print globalvars.get_time(), '添加pinggu_xiangmufuzeren数据（哈尔滨）'
  insert_data_hrb()

  print globalvars.get_time(), '修正评估类别'
  update_leibie()

  print globalvars.get_time(), '修正资格证编号'
  update_zigezheng()

  print globalvars.get_time(), '修正上岗证编号'
  update_shanggangzheng()

def insert_data_hlj():
  cursor = globalvars.cnx2.cursor()
  sql = ('SELECT * FROM tbs001_projectleader '
         'JOIN tbs001_evaluationunit '
         'ON (tbs001_projectleader.unitid='
         'tbs001_evaluationunit.id) '
         'ORDER BY tbs001_projectleader.id')
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('SELECT * FROM pinggu_danwei '
           'WHERE MingCheng=%s')
    param = (row[9],)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    danwei_id = data1[0][0]
    sql = ('INSERT INTO pinggu_xiangmufuzeren '
           '(DanWeiBianHao, XingMing, ZhengJianHao,'
           'HuanPingLeiBie, ZiGeZhengBianHao, ShangGangZhengBianHao) '
           'VALUES (%s, %s, %s, %s, %s, %s)')
    param = (danwei_id, row[1], row[3], row[4], row[7], row[8])
    cursor.execute(sql, param)

  globalvars.cnx1.commit()

def insert_data_hrb():
  cursor = globalvars.cnx3.cursor()
  sql = ( 'SELECT * FROM tbs001_projectleader '
          'JOIN tbs001_evaluationunit '
          'ON (tbs001_projectleader.unitid='
          'tbs001_evaluationunit.id) '
          'ORDER BY tbs001_projectleader.id')
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('SELECT * FROM pinggu_danwei '
                'WHERE MingCheng=%s')
    param = (row[9],)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    danwei_id = data1[0][0]
    sql = ('INSERT INTO pinggu_xiangmufuzeren '
           '(DanWeiBianHao, XingMing, ZhengJianHao,'
           'HuanPingLeiBie, ZiGeZhengBianHao, ShangGangZhengBianHao) '
           'VALUES (%s, %s, %s, %s, %s, %s)')
    param = (danwei_id, row[1], row[3], row[4], row[7], row[8])
    cursor.execute(sql, param)

  globalvars.cnx1.commit()

def update_leibie():
  cursor = globalvars.cnx1.cursor()
  sql = 'SELECT * FROM pinggu_xiangmufuzeren'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor3 = globalvars.cnx3.cursor()
  for row in data:
    sql = ('SELECT * '
           'FROM tbs001_basicdatasub '
           'WHERE id=%s')
    param = (row[4],)
    cursor3.execute(sql, param)
    row3 = cursor3.fetchone()
    if row3 != None:
      sql = ('UPDATE pinggu_xiangmufuzeren '
             'SET HuanPingLeiBie=%s '
             'WHERE id=%s')
      param = (row3[2], row[0])
      cursor.execute(sql, param)

  globalvars.cnx1.commit()

def update_zigezheng():
  cursor = globalvars.cnx1.cursor()
  sql = 'SELECT * FROM pinggu_xiangmufuzeren'
  cursor.execute(sql)
  data = cursor.fetchall()
  for row in data:
    if row[5] != '' and row[5] != None:
      text = row[5].upper().replace('附件\\', '')
      text = text.replace('CERTIFICATEPIC.JPG', '')
      text = text.replace('CERTIFICATEPIC.PNG', '')
      sql = ('UPDATE pinggu_xiangmufuzeren '
             'SET ZiGeZhengBianHao=%s '
             'WHERE id=%s')
      param = (text, row[0])
      cursor.execute(sql, param)

  globalvars.cnx1.commit()

def update_shanggangzheng():
  cursor = globalvars.cnx1.cursor()
  sql = 'SELECT * FROM pinggu_xiangmufuzeren'
  cursor.execute(sql)
  data = cursor.fetchall()
  for row in data:
    if row[6] != '' and row[6] != None:
      text = row[6].upper().replace('附件\\', '')
      text = text.replace('APPOINTMENTCARDPIC.JPG', '')
      text = text.replace('APPOINTMENTCARDPIC.PNG', '')
      sql = ('UPDATE pinggu_xiangmufuzeren '
             'SET ShangGangZhengBianHao=%s'
             'WHERE id=%s')
      param = (text, row[0])
      cursor.execute(sql, param)
  globalvars.cnx1.commit()
