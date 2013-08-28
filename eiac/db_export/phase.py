# -*- coding:utf-8 -*-

import globalvars

def run():
  print globalvars.get_time(), '清空phase表'
  globalvars.trunc_phase()

  print globalvars.get_time(), '添加phase数据（黑龙江）'
  insert_data_hlj()

  print globalvars.get_time(), '添加phase数据（哈尔滨）'
  insert_data_hrb()

def insert_data_hlj():
  cursor = globalvars.cnx2.cursor()
  sql = 'SELECT * FROM tbs001_developprojectbasicinfo'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ( 'INSERT INTO phase_a1 '
            '(ZhuangTai, DiQu ,XiangMuMingCheng,'
            'JianSheDiDian, DiQuDaiMa1, DiQuDaiMa2,'
            'XiangMuLianXiRen, LianXiRenDianHua, BaoGaoShuBiao,'
            'HuanBaoTouZi, ZongTouZi, SuoZhanBiLi,'
            'PingJiaJingFei, HangYeLeiBie1, HangYeLeiBie2,'
            'HangYeLeiBie3, HuanPingLeiBie, HuanTongLeiBie,'
            'JianSheXingZhi, JianSheNeirong, XiangMuMiaoShu) '
            'VALUES (%s, %s, %s, %s, %s, %s,'
            '%s, %s, %s, %s, %s, %s,'
            '%s, %s, %s, %s, %s, %s,'
            '%s, %s, %s)')
    param = ( '提交', '黑龙江', row[0], row[2], row[15], '',
              row[4], row[5], row[12], row[17], row[6], row[18],
              row[106], row[7], row[8], row[9], row[11], row[10],
              '', row[13], row[102])
    cursor.execute(sql, param)
    pid = cursor.lastrowid
    phase_a2(row, pid)
    phase_a3(row, pid)
    phase_b1_hlj(row, pid)
    phase_b2(row, pid)
    phase_b3(row, pid)
    phase_b4(row, pid)
    phase_b5_hlj(row, pid)
    phase_b6(row, pid)
    phase_b7(row, pid)
    phase_b8(row, pid)
    phase_config_hlj(row, pid)

  globalvars.cnx1.commit()

def insert_data_hrb():
  cursor = globalvars.cnx3.cursor()
  sql = 'SELECT * FROM tbs001_developprojectbasicinfo'
  cursor.execute(sql)
  data = cursor.fetchall()

  cursor = globalvars.cnx1.cursor()
  for row in data:
    sql = ( 'INSERT INTO phase_a1 '
            '(ZhuangTai, DiQu, XiangMuMingCheng,'
            'JianSheDiDian, DiQuDaiMa1, DiQuDaiMa2,'
            'XiangMuLianXiRen, LianXiRenDianHua, BaoGaoShuBiao,'
            'HuanBaoTouZi, ZongTouZi, SuoZhanBiLi,'
            'PingJiaJingFei, HangYeLeiBie1, HangYeLeiBie2,'
            'HangYeLeiBie3, HuanPingLeiBie, HuanTongLeiBie,'
            'JianSheXingZhi, JianSheNeirong, XiangMuMiaoShu) '
            'VALUES (%s, %s, %s, %s, %s, %s,'
            '%s, %s, %s, %s, %s, %s,'
            '%s, %s, %s, %s, %s, %s,'
            '%s, %s, %s)')
    param = ( '提交', '哈尔滨', row[0], row[2], row[15], '',
              row[4], row[5], row[12], row[17], row[6], row[18],
              row[106], row[7], row[8], row[9], row[11], row[10],
              '', row[13], row[102])
    cursor.execute(sql, param)
    pid = cursor.lastrowid
    phase_a2(row, pid)
    phase_a3(row, pid)
    phase_b1_hrb(row, pid)
    phase_b2(row, pid)
    phase_b3(row, pid)
    phase_b4(row, pid)
    phase_b5_hrb(row, pid)
    phase_b6(row, pid)
    phase_b7(row, pid)
    phase_b8(row, pid)
    phase_config_hrb(row, pid)

  globalvars.cnx1.commit()

def phase_a2(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_a2 '
          'VALUES (%s, %s, %s, %s, %s)')
  param = (row_id, row[101], row[107], row[118], row[105])
  cursor.execute(sql, param)

def phase_a3(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = 'INSERT INTO phase_a3 VALUES (%s, %s)'
  param = (row_id, row[100])
  cursor.execute(sql, param)

def phase_b1_hlj(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b1 '
          'VALUES (%s, %s, %s, %s, %s, %s,'
          '%s, %s)')
  param = ( row_id, row[59], row[58], row[60], row[61], row[62],
            row[137], row[29])
  cursor.execute(sql, param)

def phase_b1_hrb(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b1 '
          'VALUES (%s, %s, %s, %s, %s, %s,'
          '%s, %s)')
  param = ( row_id, row[59], row[58], row[60], row[61], row[62],
            0, 0)
  cursor.execute(sql, param)

def phase_b2(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = 'INSERT INTO phase_b2 VALUES (%s, %s)'
  param = (row_id, row[63])
  cursor.execute(sql, param)

def phase_b3(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = 'INSERT INTO phase_b3 VALUES (%s, %s)'
  param = (row_id, row[66])
  cursor.execute(sql, param)

def phase_b4(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = 'INSERT INTO phase_b4 VALUES (%s, %s, %s, %s)'
  param = (row_id, row[72], row[37], row[71])
  cursor.execute(sql, param)

def phase_b5_hlj(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = 'INSERT INTO phase_b5 VALUES (%s, %s, %s, %s, %s)'
  param = (row_id, row[80], row[38], row[43], row[79])
  cursor.execute(sql, param)

def phase_b5_hrb(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = 'INSERT INTO phase_b5 VALUES (%s, %s, %s, %s, %s)'
  param = (row_id, row[80], row[38], '', row[79])
  cursor.execute(sql, param)

def phase_b6(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_b6 '
          'VALUES (%s, %s, %s, %s, %s, %s,'
          '%s, %s, %s, %s)')
  param = ( row_id, row[90], row[89], row[45], row[93], row[42],
            row[91], 0, row[92], row[108])
  cursor.execute(sql, param)

def phase_b7(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = 'INSERT INTO phase_b7 VALUES (%s, %s, %s, %s, %s)'
  param = (row_id, row[96], row[97], row[142], '0')
  cursor.execute(sql, param)

def phase_b8(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = 'INSERT INTO phase_b8 VALUES (%s, %s, %s)'
  param = (row_id, row[99], row[143])
  cursor.execute(sql, param)

def phase_config_hlj(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_config '
          'VALUES (%s, %s, %s, %s, %s, %s,'
          '%s, %s, %s, %s, %s, %s,'
          '%s)')
  param = ( row_id, '', row[103], row[104], '0', '',
            '', row[26], row[27], row[28], row[29], row[144],
            0)
  cursor.execute(sql, param)

def phase_config_hrb(row, row_id):
  cursor = globalvars.cnx1.cursor()
  sql = ( 'INSERT INTO phase_config '
          'VALUES (%s, %s, %s, %s, %s, %s,'
          '%s, %s, %s, %s, %s, %s,'
          '%s)')
  param = ( row_id, '', row[103], row[104], row[146], row[145],
            row[151], row[26], row[27], row[28], row[29], row[144],
            row[147])
  cursor.execute(sql, param)
