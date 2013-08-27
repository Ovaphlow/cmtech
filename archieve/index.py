# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector

def run():
  cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
  cursor = cnx.cursor()
  sql = ( 'SELECT * FROM update_log '
          'ORDER BY id DESC')
  cursor.execute(sql)
  data = cursor.fetchall()
  cursor.close()
  cnx.close()
  template_param = {
    'data': data
  }
  template = globalvars.jinja_env.get_template('template/index.html')
  return template.render(template_param)
