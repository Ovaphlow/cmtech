# -*- coding:utf-8 -*-

import time
import mysql.connector

cnx_cfg = {
  'user': 'root',
  'password': 'dsdfjk',
  'host': '127.0.0.1',
  'database': 'ems-hrb',
}

def get_time():
  return '[' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ']'

print get_time(), '连接数据库'
cnx = mysql.connector.Connect(**cnx_cfg)
