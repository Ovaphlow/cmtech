# -*- coding=UTF-8 -*-
import os


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

G_UPLOAD_PATH = os.path.join(os.getcwd(), 'static\upload')
ALLOWED_EXT = set(['jpg', 'png', 'bmp'])
G_LOCAL_PATH = 'd:\\\\archieve'
G_FILE_SERVER_ROOT = '/static/upload'


def get_time():
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def check_ext(file_name):
    return '.' in file_name and \
           file_name.rsplit('.', 1)[1] in ALLOWED_EXT


def join_file_name(sep, flist):
    s = ''
    s = '{seperator}'.format(seperator=sep).join(flist)
    return s


def get_aid(id):
    #获取档案号
    import mysql.connector

    sql = 'SELECT danganhao FROM dangan WHERE id=%s'
    param = (id, )
    cnx = mysql.connector.Connect(**cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchall()
    cursor.close()
    cnx.close()
    return data[0][0]


def get_file_path(id):
    fp = '%s\\\\%s\\\\' % (G_LOCAL_PATH, get_aid(id))
    return fp


def get_file_path1(id):
#获取上传文件地址
    fp = '%s\\%s\\' % (G_UPLOAD_PATH, get_aid(id))
    check_path(fp)
    return fp


def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


def rotate_image(file_path):
    import Image

    img = Image.open(file_path)
    img_t = img.transpose(Image.ROTATE_270)
    img_t.save(file_path)


def turn_image(file_path):
    import Image

    img = Image.open(file_path)
    img_t = img.transpose(Image.ROTATE_180)
    img_t.save(file_path)
    return True


def caozuo_jilu(id, caozuo, neirong):
    import datetime
    import mysql.connector

    date = datetime.datetime.now().strftime('%Y-%m-%d')
    time = datetime.datetime.now().strftime('%HH%MM%SS')
    sql = '''
        INSERT INTO caozuo_jilu
        (yh_id, CaoZuo, NeiRong, RiQi, ShiJian)
        VALUES(%s,%s,%s,%s,%s)
    '''
    uid = int(id)
    param = (uid, caozuo, neirong, date, time)
    cnx = mysql.connector.Connect(**cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    cnx.commit()
    cursor.close()
    cnx.close()


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
