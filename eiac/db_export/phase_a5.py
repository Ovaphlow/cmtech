# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '清空phase_a5表'
  globalvars.trunc_a5()

  print globalvars.get_time(), '添加phase_a5数据（黑龙江）'
  insert_data_hlj()

  print globalvars.get_time(), '添加phase_a5数据（哈尔滨）'
  insert_data_hrb()

def insert_data_hlj():
  cursor = globalvars.cnx2.cursor()
  sql = ('SELECT * '
         'FROM tbs001_huanjing '
         'ORDER BY id')
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ('SELECT * '
           'FROM phase_a1 '
           'WHERE XiangMuMingCheng=%s')
    param = (row[1],)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    if cursor.rowcount == 0:
      continue
    else:
      pid = data1[0][0]
      sql = 'SELECT COUNT(*) FROM phase_a5 WHERE id=%s'
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
        update_10(row, pid)
        update_11(row, pid)
        update_12(row, pid)
        update_12(row, pid)
        update_14(row, pid)
      else:
        pass

  globalvars.cnx1.commit()

def insert_data_hrb():
  cursor = globalvars.cnx3.cursor()
  sql = ( 'SELECT * '
          'FROM tbs001_huanjing '
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
      sql = 'SELECT COUNT(*) FROM phase_a5 WHERE id=%s'
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
        update_10(row, pid)
        update_11(row, pid)
        update_12(row, pid)
        update_12(row, pid)
        update_14(row, pid)
      else:
        pass

  globalvars.cnx1.commit()

def insert(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ('INSERT INTO phase_a5 '
         '(id) '
         'VALUES (%s)')
  param = (pid,)
  cursor.execute(sql, param)

def update_1(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ('UPDATE phase_a5 '
         'SET '
         'FS_1_1=%s,FS_1_2=%s,FS_1_3=%s,'
         'FS_1_4=%s,FS_2_1=%s,FS_2_2=%s,'
         'FS_2_3=%s,FS_2_4=%s,FS_2_5=%s,'
         'FS_2_6=%s,FS_3_1=%s,FS_3_2=%s,'
         'FS_3_3=%s,FS_3_4=%s,FS_3_5=%s '
         'WHERE id=%s')
  param = (row[19], row[20], row[21],
           row[22], row[23], row[24],
           row[25], row[26], row[27],
           row[28], row[29], row[30],
           row[31], row[32], row[33],
           pid)
  cursor.execute(sql, param)

def update_2(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'HXXYL_1_1=%s,HXXYL_1_2=%s,HXXYL_1_3=%s,'
          'HXXYL_1_4=%s,HXXYL_2_1=%s,HXXYL_2_2=%s,'
          'HXXYL_2_3=%s,HXXYL_2_4=%s,HXXYL_2_5=%s,'
          'HXXYL_2_6=%s,HXXYL_3_1=%s,HXXYL_3_2=%s,'
          'HXXYL_3_3=%s,HXXYL_3_4=%s,HXXYL_3_5=%s '
          'WHERE id=%s')
  param = ( row[34], row[35], row[36],
            row[37], row[38], row[39],
            row[40], row[41], row[42],
            row[43], row[44], row[45],
            row[46], row[47], row[48],
            pid)
  cursor.execute(sql, param)

def update_3(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'AD_1_1=%s,AD_1_2=%s,AD_1_3=%s,'
          'AD_1_4=%s,AD_2_1=%s,AD_2_2=%s,'
          'AD_2_3=%s,AD_2_4=%s,AD_2_5=%s,'
          'AD_2_6=%s,AD_3_1=%s,AD_3_2=%s,'
          'AD_3_3=%s,AD_3_4=%s,AD_3_5=%s '
          'WHERE id=%s')
  param = ( row[49], row[50], row[51],
            row[52], row[53], row[54],
            row[55], row[56], row[57],
            row[58], row[59], row[60],
            row[61], row[62], row[63],
            pid)
  cursor.execute(sql, param)

def update_4(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'SY_1_1=%s,SY_1_2=%s,SY_1_3=%s,'
          'SY_1_4=%s,SY_2_1=%s,SY_2_2=%s,'
          'SY_2_3=%s,SY_2_4=%s,SY_2_5=%s,'
          'SY_2_6=%s,SY_3_1=%s,SY_3_2=%s,'
          'SY_3_3=%s,SY_3_4=%s,SY_3_5=%s '
          'WHERE id=%s')
  param = ( row[64], row[65], row[66],
            row[67], row[68], row[69],
            row[70], row[71], row[72],
            row[73], row[74], row[75],
            row[76], row[77], row[78],
            pid)
  cursor.execute(sql, param)

def update_5(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'FQ_1_1=%s,FQ_1_2=%s,FQ_1_3=%s,'
          'FQ_1_4=%s,FQ_2_1=%s,FQ_2_2=%s,'
          'FQ_2_3=%s,FQ_2_4=%s,FQ_2_5=%s,'
          'FQ_2_6=%s,FQ_3_1=%s,FQ_3_2=%s,'
          'FQ_3_3=%s,FQ_3_4=%s,FQ_3_5=%s '
          'WHERE id=%s')
  param = ( row[79], row[80], row[81],
            row[82], row[83], row[84],
            row[85], row[86], row[87],
            row[88], row[89], row[90],
            row[91], row[92], row[93],
            pid)
  cursor.execute(sql, param)

def update_6(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'EYHL_1_1=%s,EYHL_1_2=%s,EYHL_1_3=%s,'
          'EYHL_1_4=%s,EYHL_2_1=%s,EYHL_2_2=%s,'
          'EYHL_2_3=%s,EYHL_2_4=%s,EYHL_2_5=%s,'
          'EYHL_2_6=%s,EYHL_3_1=%s,EYHL_3_2=%s,'
          'EYHL_3_3=%s,EYHL_3_4=%s,EYHL_3_5=%s '
          'WHERE id=%s')
  param = ( row[94], row[95], row[96],
            row[97], row[98], row[99],
            row[100], row[101], row[102],
            row[103], row[104], row[105],
            row[106], row[107], row[108],
            pid)
  cursor.execute(sql, param)

def update_7(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'YCh_1_1=%s,YCh_1_2=%s,YCh_1_3=%s,'
          'YCh_1_4=%s,YCh_2_1=%s,YCh_2_2=%s,'
          'YCh_2_3=%s,YCh_2_4=%s,YCh_2_5=%s,'
          'YCh_2_6=%s,YCh_3_1=%s,YCh_3_2=%s,'
          'YCh_3_3=%s,YCh_3_4=%s,YCh_3_5=%s '
          'WHERE id=%s')
  param = ( row[109], row[110], row[111],
            row[112], row[113], row[114],
            row[115], row[116], row[117],
            row[118], row[119], row[120],
            row[121], row[122], row[123],
            pid)
  cursor.execute(sql, param)

def update_8(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'GYFM_1_1=%s,GYFM_1_2=%s,GYFM_1_3=%s,'
          'GYFM_1_4=%s,GYFM_2_1=%s,GYFM_2_2=%s,'
          'GYFM_2_3=%s,GYFM_2_4=%s,GYFM_2_5=%s,'
          'GYFM_2_6=%s,GYFM_3_1=%s,GYFM_3_2=%s,'
          'GYFM_3_3=%s,GYFM_3_4=%s,GYFM_3_5=%s '
          'WHERE id=%s')
  param = ( row[124], row[125], row[126],
            row[127], row[128], row[129],
            row[130], row[131], row[132],
            row[133], row[134], row[135],
            row[136], row[137], row[138],
            pid)
  cursor.execute(sql, param)

def update_9(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'DYHHW_1_1=%s,DYHHW_1_2=%s,DYHHW_1_3=%s,'
          'DYHHW_1_4=%s,DYHHW_2_1=%s,DYHHW_2_2=%s,'
          'DYHHW_2_3=%s,DYHHW_2_4=%s,DYHHW_2_5=%s,'
          'DYHHW_2_6=%s,DYHHW_3_1=%s,DYHHW_3_2=%s,'
          'DYHHW_3_3=%s,DYHHW_3_4=%s,DYHHW_3_5=%s '
          'WHERE id=%s')
  param = ( row[139], row[140], row[141],
            row[142], row[143], row[144],
            row[145], row[146], row[147],
            row[148], row[149], row[150],
            row[151], row[152], row[153],
            pid)
  cursor.execute(sql, param)

def update_10(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'GYGTFW_1_1=%s,GYGTFW_1_2=%s,GYGTFW_1_3=%s,'
          'GYGTFW_1_4=%s,GYGTFW_2_1=%s,GYGTFW_2_2=%s,'
          'GYGTFW_2_3=%s,GYGTFW_2_4=%s,GYGTFW_2_5=%s,'
          'GYGTFW_2_6=%s,GYGTFW_3_1=%s,GYGTFW_3_2=%s,'
          'GYGTFW_3_3=%s,GYGTFW_3_4=%s,GYGTFW_3_5=%s '
          'WHERE id=%s')
  param = ( row[154], row[155], row[156],
            row[157], row[158], row[159],
            row[160], row[161], row[162],
            row[163], row[164], row[165],
            row[166], row[167], row[168],
            pid)
  cursor.execute(sql, param)

def update_11(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'QTXG1_1_1=%s,QTXG1_1_2=%s,QTXG1_1_3=%s,'
          'QTXG1_1_4=%s,QTXG1_2_1=%s,QTXG1_2_2=%s,'
          'QTXG1_2_3=%s,QTXG1_2_4=%s,QTXG1_2_5=%s,'
          'QTXG1_2_6=%s,QTXG1_3_1=%s,QTXG1_3_2=%s,'
          'QTXG1_3_3=%s,QTXG1_3_4=%s,QTXG1_3_5=%s '
          'WHERE id=%s')
  param = ( row[169], row[170], row[171],
            row[172], row[173], row[174],
            row[175], row[176], row[177],
            row[178], row[179], row[180],
            row[181], row[182], row[183],
            pid)
  cursor.execute(sql, param)

def update_12(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'QTXG2_1_1=%s,QTXG2_1_2=%s,QTXG2_1_3=%s,'
          'QTXG2_1_4=%s,QTXG2_2_1=%s,QTXG2_2_2=%s,'
          'QTXG2_2_3=%s,QTXG2_2_4=%s,QTXG2_2_5=%s,'
          'QTXG2_2_6=%s,QTXG2_3_1=%s,QTXG2_3_2=%s,'
          'QTXG2_3_3=%s,QTXG2_3_4=%s,QTXG2_3_5=%s '
          'WHERE id=%s')
  param = ( row[184], row[185], row[186],
            row[187], row[188], row[189],
            row[190], row[191], row[192],
            row[193], row[194], row[195],
            row[196], row[197], row[198],
            pid)
  cursor.execute(sql, param)

def update_13(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'QTXG3_1_1=%s,QTXG3_1_2=%s,QTXG3_1_3=%s,'
          'QTXG3_1_4=%s,QTXG3_2_1=%s,QTXG3_2_2=%s,'
          'QTXG3_2_3=%s,QTXG3_2_4=%s,QTXG3_2_5=%s,'
          'QTXG3_2_6=%s,QTXG3_3_1=%s,QTXG3_3_2=%s,'
          'QTXG3_3_3=%s,QTXG3_3_4=%s,QTXG3_3_5=%s '
          'WHERE id=%s')
  param = ( row[199], row[200], row[201],
            row[202], row[203], row[204],
            row[205], row[206], row[207],
            row[208], row[209], row[210],
            row[211], row[212], row[213],
            pid)
  cursor.execute(sql, param)

def update_14(row, pid):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'UPDATE phase_a5 '
          'SET '
          'QTXG4_1_1=%s,QTXG4_1_2=%s,QTXG4_1_3=%s,'
          'QTXG4_1_4=%s,QTXG4_2_1=%s,QTXG4_2_2=%s,'
          'QTXG4_2_3=%s,QTXG4_2_4=%s,QTXG4_2_5=%s,'
          'QTXG4_2_6=%s,QTXG4_3_1=%s,QTXG4_3_2=%s,'
          'QTXG4_3_3=%s,QTXG4_3_4=%s,QTXG4_3_5=%s '
          'WHERE id=%s')
  param = ( row[214], row[215], row[216],
            row[217], row[218], row[219],
            row[220], row[221], row[222],
            row[223], row[224], row[225],
            row[226], row[227], row[228],
            pid)
  cursor.execute(sql, param)
