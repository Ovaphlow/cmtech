# -*- coding=UTF-8 -*-
#import os
import mysql.connector

'''
jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
'''

cnx_cfg = {
    'user': 'cmtech',
    'password': 'cmtech.1123',
    'host': '125.211.221.215',
    'database': 'cm_archieve',
}

G_UPLOAD_PATH = 'd:\\archieve'
ALLOWED_EXT = set(['jpg', 'png', 'bmp'])
G_LOCAL_PATH = 'd:\\\\archieve'


def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


def check_ext(file_name):
    return '.' in file_name and \
        file_name.rsplit('.', 1)[1] in ALLOWED_EXT


def join_file_name(sep, flist):
    s = ''
    s = '{seperator}'.format(seperator=sep).join(flist)
    return s

def get_file_path(id):
    sql = 'SELECT danganhao FROM dangan WHERE id=%s'
    param = (id, )
    cnx = mysql.connector.Connect(**cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchall()
    cursor.close()
    cnx.close()
    aid = data[0][0]
    fp = '%s\\\\%s\\\\' % (G_LOCAL_PATH, aid)
    return fp
