# -*- coding=UTF-8 -*-
import jinja2
#import os

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

G_UPLOAD_PATH = 'd:\\1123'
ALLOWED_EXT = set(['jpg', 'png', 'bmp'])

def get_time():
  return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def check_ext(file_name):
  return '.' in file_name and \
    file_name.rsplit('.', 1)[1] in ALLOWED_EXT
