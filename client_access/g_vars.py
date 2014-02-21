# -*- coding=UTF-8 -*-

cnx_param = {
    'user': 'root',
    'password': 'dsdfjk',
    'host': '127.0.0.1',
    'database': 'cm_archieve',
}
"""
生产环境
cnx_param = {
    'user': 'root',
    'password': 'dsdfjk',
    'host': '127.0.0.1',
    'database': 'cm_archieve',
}
开发环境
cnx_param = {
    'user': 'cmtech',
    'password': 'cmtech.1123',
    'host': '125.211.221.215',
    'database': 'cm_archieve',
}
"""

G_FILE_SERVER_ROOT = 'http://127.0.0.1:5000/static/upload'
"""
生产环境
G_FILE_SERVER_ROOT = 'http://172.17.203.100:5000/static/upload'
开发环境
G_FILE_SERVER_ROOT = 'http://127.0.0.1:5000/static/upload'
"""

cat_name = [
    u'就业类',
    u'职工历年调整工资审批表',
    u'职工登记表',
    u'历次调转介绍信',
    u'养老保险转移单与解除关系备案登记表',
    u'职称材料',
    u'学历材料',
    u'入党、团及职务变动',
    u'其它',
]


def connect_db():
    import mysql.connector
    return mysql.connector.Connect(**cnx_param)


def close_db(cursor, cnx):
    cursor.close()
    cnx.close()
