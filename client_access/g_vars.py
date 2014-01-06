# -*- coding=UTF-8 -*-

cnx_param = {
    'user': 'cmtech',
    'password': 'cmtech.1123',
    'host': '125.211.221.215',
    'database': 'cm_archieve',
}


def connect_db():
    import mysql.connector
    return mysql.connector.Connect(**cnx_param)


def close_db(cursor, cnx):
    cursor.close()
    cnx.close()
