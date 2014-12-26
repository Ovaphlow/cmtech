# -*- coding=UTF-8 -*-
import xlrd, mysql.connector
import sys, os
sys.path.append('..')
import globalvars


if __name__ == '__main__':
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    print u'连接数据库'
    cursor = cnx.cursor()
    print u'数据库游标'
    sql = 'SELECT * FROM dangan LIMIT 10'
    cursor.execute(sql)
    print u'执行查询'
    data = cursor.fetchall()
    print u'获取数据'
    for row in data:
        years = globalvars.get_years(row[4], row[11], row[10])
        dob_y = row[5][0:4]
        dor = '%s%s' % (int(dob_y) + years, row[5][4:])
        if dor == row[6]:
            continue
        else:
            print row[2], u'特:', row[11], u'女:', row[10], u'更正数据', row[6], '->', dor
            sql = '''
                UPDATE dangan
                SET YuTuiXiuRiQi=%s
                WHERE id=%s
            '''
            param = (dor, row[0])
            cursor.execute(sql, param)
    cnx.commit()
    cursor.close()
    cnx.close()