# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '清空jianshe_danwei表'
  globalvars.trunc_jshdw()

  print globalvars.get_time(), '添加jianshe_danwei数据（黑龙江）'
  insert_data_hlj()
  print globalvars.get_time(), '添加jianshe_danwei数据（哈尔滨）'
  insert_data_hrb()

def insert_data_hlj():
  cursor = globalvars.cnx2.cursor()
  sql = 'SELECT * FROM tbs001_constructionunit'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('INSERT INTO jianshe_danwei '
           '(MingCheng, DianYou, DiZhi, YouBian, FaRen, '
           'LianXiRen, DianHua, ChuanZhen) '
           'VALUES (%s, %s, %s, %s, %s, %s,'
           '%s, %s)')
    param = (row[1], row[10], row[2], row[4], row[8], row[7],
             row[3], row[9])
    cursor.execute(sql, param)

  globalvars.cnx1.commit()

def insert_data_hrb():
  cursor = globalvars.cnx3.cursor()
  sql = 'SELECT * FROM tbs001_constructionunit'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('INSERT INTO jianshe_danwei '
           '(MingCheng, DianYou, DiZhi, YouBian, FaRen, '
           'LianXiRen, DianHua, ChuanZhen) '
           'VALUES (%s, %s, %s, %s, %s, %s,'
           '%s, %s)')
    param = (row[1], row[10], row[2], row[4], row[8], row[7],
             row[3], row[9])
    cursor.execute(sql, param)

  globalvars.cnx1.commit()
