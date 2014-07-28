# -*- coding=UTF-8 -*-

import datetime
import time
import os

import mysql.connector

from PIL import Image, ImageDraw, ImageFont
from sqlalchemy import create_engine


'''
jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
'''

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

db_engine = create_engine('mysql+mysqlconnector://%s:%s@%s/%s' % \
    (cnx_cfg['user'],cnx_cfg['password'], \
    cnx_cfg['host'],cnx_cfg['database']),
    pool_recycle=900,
    pool_size=5)

G_UPLOAD_PATH = os.path.join(os.getcwd(), 'static\upload')
ALLOWED_EXT = set(['jpg', 'png', 'bmp'])
G_LOCAL_PATH = 'd:\\\\archieve'
G_FILE_SERVER_ROOT = '/static/upload'
G_ADMIN_USER = ['admin']
G_VIEW_USER = ['test1123']


def connect_db():
    return mysql.connector.Connect(**cnx_cfg)


def close_db(cursor, cnx):
    cursor.close()
    cnx.close()


def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def check_ext(file_name):
    return '.' in file_name and \
           file_name.rsplit('.', 1)[1] in ALLOWED_EXT


def join_file_name(sep, flist):
    # s = ''
    s = '{seperator}'.format(seperator=sep).join(flist)
    return s


def get_aid(rec_id):
    # 获取档案号
    sql = 'SELECT danganhao FROM dangan WHERE id=%s'
    param = (rec_id,)
    cnx = connect_db()
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchall()
    close_db(cursor, cnx)
    return data[0][0]


def get_file_path(rec_id):
    fp = '%s\\\\%s\\\\' % (G_LOCAL_PATH, get_aid(rec_id))
    return fp


def get_file_path1(rec_id):
# 获取上传文件地址
    fp = '%s\\%s\\' % (G_UPLOAD_PATH, get_aid(rec_id))
    check_path(fp)
    return fp


def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


def rotate_image(file_path):
    img = Image.open(file_path)
    img_t = img.transpose(Image.ROTATE_270)
    img_t.save(file_path)


def turn_image(file_path):
    img = Image.open(file_path)
    img_t = img.transpose(Image.ROTATE_180)
    img_t.save(file_path)
    return True


def caozuo_jilu(user_id, caozuo, neirong):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    time = datetime.datetime.now().strftime('%H:%M:%S')
    sql = '''
        insert into caozuo_jilu
            (yh_id,CaoZuo,NeiRong,RiQi,ShiJian)
        values
            (:yh_id,:caozuo,:neirong,:riqi,:shijian)
    '''
    uid = int(user_id)
    param = {'yh_id': uid,
        'caozuo': caozuo,
        'neirong': neirong,
        'riqi': date,
        'shijian': time}
    db_engine.execute(text(' '.join(sql.split())), param)


def get_years(gender, te, nv):
    if gender == u'男':
        if te == 1:
            years = 55
        else:
            years = 60
    else:
        if te == 1:
            years = 45
        else:
            if nv == 1:
                years = 55
            else:
                years = 50
    return years


def idcard_convert(idcard_15):
    wi = ['7', '9', '10', '5', '8', '4', '2', '1', '6', '3', '7', '9', '10', '5', '8', '4', '2']
    ai = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    idcard_18 = '%s19%s' % (idcard_15[0:6], idcard_15[6:15])
    i = 0
    sum_a = 0
    for c in idcard_18:
        sum_t = int(c) * int(wi[i])
        sum_a += sum_t
        i += 1
    idcard_18 = '%s%s' % (idcard_18, ai[sum_a % 11])
    return idcard_18


def render_text(file_name, font_size, text, output_name, output_type):
    img = Image.open(file_name)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('c:\\windows\\fonts\\simhei.ttf', font_size)
    draw.text((10, 20), text, font=font, fill=(255, 0, 0, 255))
    img.save(output_name, output_type)
    # img.show()
