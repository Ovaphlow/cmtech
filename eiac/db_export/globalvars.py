# -*- coding:utf-8 -*-

import time
import mysql.connector

cnx1_cfg = {
  'user': 'root',
  'password': 'dsdfjk',
  'host': '127.0.0.1',
  'database': 'eiac-sys',
}

cnx2_cfg = {
  'user': 'root',
  'password': 'dsdfjk',
  'host': '127.0.0.1',
  'database': 'emsdatabase',
}

cnx3_cfg = {
  'user': 'root',
  'password': 'dsdfjk',
  'host': '127.0.0.1',
  'database': 'ems-hrb',
}

def get_time():
  return '[' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ']'

def trunc_jshdw():
  cursor = cnx1.cursor()
  sql = 'TRUNCATE TABLE jianshe_danwei'
  cursor.execute(sql)
  cnx1.commit()

def trunc_staff():
  cursor = cnx1.cursor()
  sql = 'TRUNCATE TABLE staff'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE authority'
  cursor.execute(sql)
  cnx1.commit()

def trunc_pgdw():
  cursor = cnx1.cursor()
  sql = 'TRUNCATE TABLE pinggu_danwei'
  cursor.execute(sql)
  cnx1.commit()

def trunc_xmfzr():
  cursor = cnx1.cursor()
  sql = 'TRUNCATE TABLE pinggu_xiangmufuzeren'
  cursor.execute(sql)
  cnx1.commit()

def trunc_zhuanjia():
  cursor = cnx1.cursor()
  sql = 'TRUNCATE TABLE zhuanjia'
  cursor.execute(sql)
  cnx1.commit()

def trunc_phase():
  cursor = cnx1.cursor()
  sql = 'TRUNCATE TABLE phase_a1'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_a2'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_a3'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_a4'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_a5'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_a6'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_b1'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_b2'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_b3'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_b4'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_b4'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_b5'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_b6'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_b7'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_b8'
  cursor.execute(sql)
  sql = 'TRUNCATE TABLE phase_config'
  cursor.execute(sql)
  cnx1.commit()

def trunc_log():
  cursor = cnx1.cursor()
  sql = 'TRUNCATE TABLE phase_b_log'
  cursor.execute(sql)
  cnx1.commit()

def trunc_a4():
  cursor = cnx1.cursor()
  sql = 'TRUNCATE TABLE phase_a4'
  cursor.execute(sql)
  cnx1.commit()

def trunc_a5():
  cursor = cnx1.cursor()
  sql = 'TRUNCATE TABLE phase_a5'
  cursor.execute(sql)
  cnx1.commit()

def trunc_a6():
  cursor = cnx1.cursor()
  sql = 'TRUNCATE TABLE phase_a6'
  cursor.execute(sql)
  cnx1.commit()

print get_time(), '连接V3数据库'
cnx1 = mysql.connector.Connect(**cnx1_cfg)

print get_time(), '连接V2黑龙江数据库'
cnx2 = mysql.connector.Connect(**cnx2_cfg)

print get_time(), '连接V2哈尔滨数据库'
cnx3 = mysql.connector.Connect(**cnx3_cfg)
