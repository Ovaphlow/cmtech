# -*- coding:utf-8 -*-

import sys
import globalvars

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
  cursor = globalvars.cnx1.cursor()
  sql = 'SELECT * FROM staff'
  cursor.execute(sql)
  data = cursor.fetchall()

  for row in data:
    print row[1], row[2], row[3], row[5]
