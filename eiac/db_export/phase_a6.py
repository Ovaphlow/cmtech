# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '清空phase_a6表'
  globalvars.trunc_a6()

  print globalvars.get_time(), '添加phase_a6数据（黑龙江）'
  insert_data_hlj()

  print globalvars.get_time(), '添加phase_a6数据（哈尔滨）'
  insert_data_hrb()

def insert_data_hlj():
  cursor = globalvars.cnx2.cursor()
  sql = ( 'SELECT * '
          'FROM tbx001_shengtai '
          'ORDER BY id')
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ( 'SELECT * '
            'FROM phase_a1 '
            'WHERE XiangMuMingCheng=%s')
    param = (row[1],)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    if cursor.rowcount == 0:
      continue
    else:
      pid = data1[0][0]
      sql = 'SELECT COUNT(*) FROM phase_a6 WHERE id=%s'
      param = (pid,)
      cursor.execute(sql, param)
      row1 = cursor.fetchone()
      if row1[0] == 0:
        insert(row, pid)
        update_1(row, pid)
        update_2(row, pid)
        update_3(row, pid)
        update_4(row, pid)
        update_5(row, pid)
        update_6(row, pid)
        update_7(row, pid)
        update_8(row, pid)
        update_9(row, pid)
      else:
        pass

  globalvars.cnx1.commit()

def insert_data_hrb():
  cursor = globalvars.cnx3.cursor()
  sql = ( 'SELECT * '
          'FROM tbx001_shengtai '
          'ORDER BY id')
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ( 'SELECT * '
            'FROM phase_a1 '
            'WHERE XiangMuMingCheng=%s')
    param = (row[1],)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    if cursor.rowcount == 0:
      continue
    else:
      pid = data1[0][0]
      sql = 'SELECT COUNT(*) FROM phase_a6 WHERE id=%s'
      param = (pid,)
      cursor.execute(sql, param)
      row1 = cursor.fetchone()
      if row1[0] == 0:
        insert(row, pid)
        update_1(row, pid)
        update_2(row, pid)
        update_3(row, pid)
        update_4(row, pid)
        update_5(row, pid)
        update_6(row, pid)
        update_7(row, pid)
        update_8(row, pid)
        update_9(row, pid)
      else:
        pass

  globalvars.cnx1.commit()

def insert(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_a6 '
          '(id) '
          'VALUES (%s)')
  param = (pid,)
  cursor.execute(sql, param)

def update_1(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a6 '
          'SET '
          'ZRBHQ_1=%s,ZRBHQ_2=%s,ZRBHQ_3=%s,'
          'ZRBHQ_4=%s,ZRBHQ_5=%s,ZRBHQ_6=%s,'
          'ZRBHQ_7=%s,ZRBHQ_8=%s,ZRBHQ_9=%s,'
          'ZRBHQ_10=%s '
          'WHERE id=%s')
  param = ( row[2], row[3], row[4],
            row[5], row[6], row[7],
            row[8], row[9], row[10],
            row[11], pid)
  cursor.execute(sql, param)

def update_2(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a6 '
          'SET '
          'ShYBHQ_1=%s,ShYBHQ_2=%s,ShYBHQ_3=%s,'
          'ShYBHQ_4=%s,ShYBHQ_5=%s,ShYBHQ_6=%s,'
          'ShYBHQ_7=%s,ShYBHQ_8=%s,ShYBHQ_9=%s,'
          'ShYBHQ_10=%s '
          'WHERE id=%s')
  param = ( row[12], row[13], row[14],
            row[15], row[16], row[17],
            row[18], row[19], row[20],
            row[21], pid)
  cursor.execute(sql, param)

def update_3(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a6 '
          'SET '
          'ZhYShD_1=%s,ZhYShD_2=%s,ZhYShD_3=%s,'
          'ZhYShD_4=%s,ZhYShD_5=%s,ZhYShD_6=%s,'
          'ZhYShD_7=%s,ZhYShD_8=%s,ZhYShD_9=%s,'
          'ZhYShD_10=%s '
          'WHERE id=%s')
  param = ( row[22], row[23], row[24],
            row[25], row[26], row[27],
            row[28], row[29], row[30],
            row[31], pid)
  cursor.execute(sql, param)

def update_4(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a6 '
          'SET '
          'FJMShQ_1=%s,FJMShQ_2=%s,FJMShQ_3=%s,'
          'FJMShQ_4=%s,FJMShQ_5=%s,FJMShQ_6=%s,'
          'FJMShQ_7=%s,FJMShQ_8=%s,FJMShQ_9=%s,'
          'FJMShQ_10=%s '
          'WHERE id=%s')
  param = ( row[32], row[33], row[34],
            row[35], row[36], row[37],
            row[38], row[39], row[40],
            row[41], pid)
  cursor.execute(sql, param)

def update_5(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a6 '
          'SET '
          'YChD_1=%s,YChD_2=%s,YChD_3=%s,'
          'YChD_4=%s,YChD_5=%s,YChD_6=%s,'
          'YChD_7=%s,YChD_8=%s,YChD_9=%s,'
          'YChD_10=%s '
          'WHERE id=%s')
  param = ( row[42], row[43], row[44],
            row[45], row[46], row[47],
            row[48], row[49], row[50],
            row[51], pid)
  cursor.execute(sql, param)

def update_6(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a6 '
          'SET '
          'ZhXTYDW_1=%s,ZhXTYDW_2=%s,ZhXTYDW_3=%s,'
          'ZhXTYDW_4=%s,ZhXTYDW_5=%s,ZhXTYDW_6=%s,'
          'ZhXTYDW_7=%s,ZhXTYDW_8=%s,ZhXTYDW_9=%s,'
          'ZhXTYDW_10=%s '
          'WHERE id=%s')
  param = ( row[52], row[53], row[54],
            row[55], row[56], row[57],
            row[58], row[59], row[60],
            row[61], pid)
  cursor.execute(sql, param)

def update_7(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a6 '
          'SET '
          'ZhXTYZhW_1=%s,ZhXTYZhW_2=%s,ZhXTYZhW_3=%s,'
          'ZhXTYZhW_4=%s,ZhXTYZhW_5=%s,ZhXTYZhW_6=%s,'
          'ZhXTYZhW_7=%s,ZhXTYZhW_8=%s,ZhXTYZhW_9=%s,'
          'ZhXTYZhW_10=%s '
          'WHERE id=%s')
  param = ( row[62], row[63], row[64],
            row[65], row[66], row[67],
            row[68], row[69], row[70],
            row[71], pid)
  cursor.execute(sql, param)

def update_8(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a6 '
          'SET '
          'ZhYTD_1_1=%s,ZhYTD_1_2=%s,ZhYTD_1_3=%s,'
          'ZhYTD_1_4=%s,ZhYTD_1_5=%s,ZhYTD_1_6=%s,'
          'ZhYTD_1_7=%s,ZhYTD_2_1=%s,ZhYTD_2_2=%s,'
          'ZhYTD_2_3=%s,ZhYTD_2_4=%s,ZhYTD_2_5=%s,'
          'ZhYTD_2_6=%s,ZhYTD_2_7=%s '
          'WHERE id=%s')
  param = ( row[72], row[73], row[74],
            row[75], row[76], row[77],
            row[78], row[79], row[80],
            row[81], row[82], row[83],
            row[84], row[85], pid)
  cursor.execute(sql, param)

def update_9(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a6 '
          'SET '
          'ZShZhL_1=%s,ZShZhL_2=%s,ZShZhL_3=%s,'
          'ZShZhL_4=%s,ZShZhL_5=%s,ZShZhL_6=%s,'
          'ChQRK_1=%s,ChQRK_2=%s,ChQRK_3=%s,'
          'ChQRK_4=%s,ChQRK_5=%s,ZhLShTLSh_1=%s,'
          'ZhLShTLSh_2=%s,ZhLShTLSh_3=%s '
          'WHERE id=%s')
  param = ( row[86], row[87], row[88],
            row[89], row[90], row[91],
            row[92], row[93], row[94],
            row[95], row[96], row[97],
            row[98], row[99],
            pid)
  cursor.execute(sql, param)
