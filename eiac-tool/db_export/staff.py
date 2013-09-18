# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '清空staff表'
  globalvars.trunc_staff()

  print globalvars.get_time(), '添加staff表数据（黑龙江）'
  insert_data_hlj()
  print globalvars.get_time(), '添加staff表数据（哈尔滨）'
  insert_data_hrb()

  print globalvars.get_time(), '添加authority表数据'
  insert_authority()

  print globalvars.get_time(), '更新authority表数据'
  update_authortity()

def insert_data_hlj():
  cursor = globalvars.cnx2.cursor()
  sql = ('SELECT * '
         'FROM tbs001_user '
         'WHERE roleid!="建设单位" '
         'AND roleid!="环评单位"')
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('INSERT INTO staff '
           '(XingMing, ZhangHao, MiMa, '
           'DianHua, ZhiWu, DiQu, '
           'DanWei) '
           'VALUES (%s, %s, %s, %s, %s, %s,'
           '%s)')
    param = (row[1], row[2], row[3], row[4], row[5], '黑龙江',
             '环评中心')
    cursor.execute(sql, param)

  globalvars.cnx1.commit()

def insert_data_hrb():
  cursor = globalvars.cnx3.cursor()
  sql = ('SELECT * '
         'FROM tbs001_user '
         'WHERE roleid!="建设单位" '
         'AND roleid!="环评单位"')
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('INSERT INTO staff '
           '(XingMing, ZhangHao, MiMa, '
           'DianHua, ZhiWu, DiQu, '
           'DanWei) '
           'VALUES (%s, %s, %s, %s, %s, cu%s,'
           '%s)')
    param = (row[1], row[2], row[3], row[4], row[5], '哈尔滨',
             '环评中心')
    cursor.execute(sql, param)

  globalvars.cnx1.commit()

def update_bumen():
  cursor = globalvars.cnx1.cursor()
  sql = ( 'SELECT * FROM staff '
          'WHERE ZhiWu LIKE "%中心领导%" OR '
          'ZhiWu LIKE "%部门负责人%" OR '
          'ZhiWu LIKE "%受理人%" OR '
          'ZhiWu LIKE "%项目负责人%"')
  cursor.execute(sql)
  data = cursor.fetchall()

  for row in data:
    if row[7] == u"黑龙江":
      cursor = globalvars.cnx2.cursor()
      sql = 'SELECT * FROM tbs001_user WHERE UserName=%s'
      param = (row[1],)
      cursor.execute(sql, param)
      data_user = cursor.fetchall()
      user_id = data_user[0][0]
      sql = ( 'SELECT * FROM tbs001_executivedepartment '
              'WHERE ed_user LIKE "%' + str(user_id) + '%"')
      cursor.execute(sql)
      data_bumen = cursor.fetchall()
      str_bumen = ''
      for row_bumen in data_bumen:
        str_bumen = str_bumen + row_bumen[1]+ ',' 
      cursor = globalvars.cnx1.cursor()
      sql = ( 'UPDATE staff '
              'SET BuMen=%s '
              'WHERE id=%s')
      param = (str_bumen, row[0])
      cursor.execute(sql, param)
    elif row[7] == u"哈尔滨":
      cursor = globalvars.cnx3.cursor()
      sql = 'SELECT * FROM tbs001_user WHERE UserName=%s'
      param = (row[1],)
      cursor.execute(sql, param)
      data_user = cursor.fetchall()
      user_id = data_user[0][0]
      sql = ( 'SELECT * FROM tbs001_executivedepartment '
              'WHERE ed_user LIKE "%' + str(user_id) + '%"')
      cursor.execute(sql)
      data_bumen = cursor.fetchall()
      str_bumen = ''
      for row_bumen in data_bumen:
        str_bumen = str_bumen + row_bumen[1]+ ',' 
      cursor = globalvars.cnx1.cursor()
      sql = ( 'UPDATE staff '
              'SET BuMen=%s '
              'WHERE id=%s')
      param = (str_bumen, row[0])
      cursor.execute(sql, param)
    else:
      pass

  globalvars.cnx1.commit()

def insert_authority():
  cursor = globalvars.cnx1.cursor()
  sql = 'SELECT id FROM staff'
  cursor.execute(sql)
  data = cursor.fetchall()

  for row in data:
    sql = ('INSERT INTO authority '
           '(staff_id) '
           'VALUES (%s)') 
    param = (row[0],)
    cursor.execute(sql, param)

  globalvars.cnx1.commit()

def update_authortity():
  cursor = globalvars.cnx1.cursor()

  sql = ( 'SELECT * FROM staff,authority '
          'WHERE staff.id=authority.staff_id '
          'AND ZhiWu LIKE "%部门负责人%"')
  cursor.execute(sql)
  data = cursor.fetchall()

  for row in data:
    sql = ( 'UPDATE authority '
            'SET b_3_1=%s, b_4_1=%s, b_4_2=%s,'
            'b_5_1=%s, b_5_2=%s, b_6_1=%s,'
            'b_7_1=%s, b_8_1=%s, b_8_2=%s '
            'WHERE staff_id=%s')
    param = ( 1, 1, 1, 1, 1, 1,
              1, 1, 1, row[10])
    cursor.execute(sql, param)

  sql = ( 'SELECT * FROM staff,authority '
          'WHERE staff.id=authority.staff_id '
          'AND ZhiWu LIKE "%中心领导%"')
  cursor.execute(sql)
  data = cursor.fetchall()

  for row in data:
    sql = ( 'UPDATE authority '
            'SET b_1_1=%s, b_1_2=%s, b_1_3=%s,'
            'b_1_4=%s, b_1_5=%s, b_2_1=%s,'
            'b_3_1=%s, b_4_1=%s, b_4_2=%s,'
            'b_5_1=%s, b_5_2=%s, b_6_1=%s,'
            'b_7_1=%s, b_8_1=%s, b_8_2=%s '
            'WHERE staff_id=%s')
    param = ( 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1,
              1, 1, 1, row[10])
    cursor.execute(sql, param)

  sql = ( 'SELECT * FROM staff,authority '
          'WHERE staff.id=authority.staff_id '
          'AND ZhiWu LIKE "%项目负责人%"')
  cursor.execute(sql)
  data = cursor.fetchall()

  for row in data:
    sql = ( 'UPDATE authority '
            'SET b_4_1=%s, b_4_2=%s, b_5_1=%s,'
            'b_5_2=%s, b_6_1=%s, b_7_1=%s,'
            'b_8_1=%s, b_8_2=%s '
            'WHERE staff_id=%s')
    param = ( 1, 1, 1, 1, 1, 1, 1, 1, row[10])
    cursor.execute(sql, param)

  sql = ( 'SELECT * FROM staff,authority '
          'WHERE staff.id=authority.staff_id '
          'AND ZhiWu LIKE "%受理人%"')
  cursor.execute(sql)
  data = cursor.fetchall()

  for row in data:
    sql = ( 'UPDATE authority '
            'SET b_1_1=%s, b_1_2=%s, b_1_3=%s,'
            'b_1_5=%s '
            'WHERE staff_id=%s')
    param = ( 1, 1, 1, 1, row[10])
    cursor.execute(sql, param)

  globalvars.cnx1.commit()

if __name__ == "__main__":
  update_bumen()