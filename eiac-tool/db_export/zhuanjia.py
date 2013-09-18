# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '清空zhuanjia表'
  globalvars.trunc_zhuanjia()

  print globalvars.get_time(), '添加zhuanjia表数据（黑龙江）'
  insert_data_hlj()

  print globalvars.get_time(), '添加zhuanjia表数据（哈尔滨）'
  insert_data_hrb()

def insert_data_hlj():
  cursor = globalvars.cnx2.cursor()
  sql = 'SELECT * FROM tbs001_expert'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('INSERT INTO zhuanjia '
                '(XingMing, XingBie, ZhiWu, '
                'ShenFenZheng, ChuShengRiQi, DanWei, '
                'GangWei, YiDongDianHua, GuDingDianHua, '
                'ChuanZhen, DianYou, ZhuanJiaLeiBie, '
                'HangYeLeiBie, PingGuLeiBie, TuiJianRen, '
                'JianJie, DengJi, DiQu) '
                'VALUES (%s, %s, %s, %s, %s, %s,'
                '%s, %s, %s, %s, %s, %s, '
                '%s, %s, %s, %s, %s, %s)')
    param = (row[1], row[2], row[3], row[5], row[4], row[6],
             row[11], row[7], row[8], row[9], row[10], row[12],
             row[13], row[14], row[15], row[16], 3, '黑龙江')
    cursor.execute(sql, param)

  globalvars.cnx1.commit()

def insert_data_hrb():
  cursor = globalvars.cnx3.cursor()
  sql = 'SELECT * FROM tbs001_expert'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('INSERT INTO zhuanjia '
                '(XingMing, XingBie, ZhiWu, '
                'ShenFenZheng, ChuShengRiQi, DanWei, '
                'GangWei, YiDongDianHua, GuDingDianHua, '
                'ChuanZhen, DianYou, ZhuanJiaLeiBie, '
                'HangYeLeiBie, PingGuLeiBie, TuiJianRen, '
                'JianJie, DengJi, DiQu) '
                'VALUES (%s, %s, %s, %s, %s, %s,'
                '%s, %s, %s, %s, %s, %s, '
                '%s, %s, %s, %s, %s, %s)')
    param = (row[1], row[2], row[3], row[5], row[4], row[6],
             row[11], row[7], row[8], row[9], row[10], row[12],
             row[13], row[14], row[15], row[16], row[19], '哈尔滨')
    cursor.execute(sql, param)

  globalvars.cnx1.commit()
