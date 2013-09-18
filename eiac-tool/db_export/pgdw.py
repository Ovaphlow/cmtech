# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '清空pinggu_danwei表'
  globalvars.trunc_pgdw()

  print globalvars.get_time(), '添加pinggu_danwei表数据（黑龙江）'
  insert_data_hlj()
  print globalvars.get_time(), '添加pinggu_danwei表数据（哈尔滨）'
  insert_data_hrb()

  print globalvars.get_time(), '添加评估单位登录信息'
  update_data_acc()

def insert_data_hlj():
  cursor = globalvars.cnx2.cursor()
  sql = 'SELECT * FROM tbs001_evaluationunit'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('INSERT INTO pinggu_danwei '
           '(MingCheng, ZhangHao, Mima,'
           'DianYou, FaRen, LianXiRen,'
           'DianHua, ChuanZhen, DiZhi,'
           'YouBian, ZhengShuBianHao, PingGuFanWei) '
           'VALUES (%s, %s, %s, %s, %s, %s,'
           '%s, %s, %s, %s, %s, %s)')
    param = (row[0], '', '', '', '', '',
             row[3], '', row[1], row[4], row[2], row[5])
    cursor.execute(sql, param)

  globalvars.cnx1.commit()

def insert_data_hrb():
  cursor = globalvars.cnx3.cursor()
  sql = 'SELECT * FROM tbs001_evaluationunit'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('INSERT INTO pinggu_danwei '
           '(MingCheng, ZhangHao, Mima,'
           'DianYou, FaRen, LianXiRen,'
           'DianHua, ChuanZhen, DiZhi,'
           'YouBian, ZhengShuBianHao, PingGuFanWei) '
           'VALUES (%s, %s, %s, %s, %s, %s,'
           '%s, %s, %s, %s, %s, %s)')
    param = (row[0], '', '', row[15], row[13], '',
             row[3], row[14], row[1], row[4], row[2], row[5])
    cursor.execute(sql, param)

  globalvars.cnx1.commit()

def update_data_acc():
  cursor = globalvars.cnx1.cursor()
  sql = 'SELECT id FROM pinggu_danwei'
  cursor.execute(sql)
  data = cursor.fetchall()
  for row in data:
    sql = ( 'UPDATE pinggu_danwei '
            'SET '
            'ZhangHao=%s,MiMa=%s '
            'WHERE id=%s')
    param = (row[0], '123456', row[0])
    cursor.execute(sql, param)
  globalvars.cnx1.commit()
