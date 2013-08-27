# -*- coding=UTF-8 -*-
import jinja2
import os

jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

cnx_cfg = {
  'user': 'root',
  'password': 'dsdfjk',
  'host': '127.0.0.1',
  'database': 'cm_archieve',
}

def get_time():
  return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
