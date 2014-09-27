# -*- coding=UTF-8 -*-

import datetime
import time
import os

from sqlalchemy import create_engine

cnx_cfg = {
    'user': 'root',
    'password': 'dsdfjk',
    'host': '127.0.0.1',
    'database': 'cm_archieve',
}
"""
生产环境
cnx_cfg = {
    'user': 'root',
    'password': 'dsdfjk',
    'host': '127.0.0.1',
    'database': 'cm_archieve',
}
开发环境
cnx_cfg = {
    'user': 'cmtech',
    'password': 'cmtech.1123',
    'host': '125.211.221.215',
    'database': 'cm_archieve',
}
"""

ARCHIEVE_FILE_URI = 'http://172.17.203.100:5000/static/upload'
# 生产环境
# ARCHIEVE_FILE_URI = 'http://172.17.203.100:5000/static/upload'
# 开发环境
# ARCHIEVE_FILE_URI = 'http://127.0.0.1:5000/static/upload'


db_engine = create_engine('mysql+mysqlconnector://%s:%s@%s/%s' % \
    (cnx_cfg['user'],cnx_cfg['password'], \
    cnx_cfg['host'],cnx_cfg['database']),
    pool_recycle=900, pool_size=5)
