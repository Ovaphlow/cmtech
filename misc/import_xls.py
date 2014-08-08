# -*- coding=UTF-8 -*-

import os
import sys

import xlrd

from sqlalchemy import text

sys.path.append('..')
from archieve.globalvars import *


if __name__ == '__main__':
    xls = xlrd.open_workbook('3.xls', 'rb')
    sh = xls.sheets()[0]
    for row in range(1, sh.nrows):
        if sh.cell(row, 6).value != u'已调入':
            print(sh.cell(row, 3).value)
            continue
        dob = sh.cell(row, 0).value
        dob = dob[6:14]
        dob = '%s-%s-%s' % (dob[0:4], dob[4:6], dob[6:8])
        dor_y = dob[0:4]
        if sh.cell(row, 2).value == u'男':
            dor = '%s-%s-%s' % (int(dor_y) + 60, dob[5:7], dob[8:10])
        else:
            dor = '%s-%s-%s' % (int(dor_y) + 50, dob[5:7], dob[8:10])
        sql = '''
            SELECT id FROM dangan WHERE DangAnHao=:archieve_id
        '''
        param = {'archieve_id': sh.cell(row, 3).value}
        res = db_engine.execute(text(' '.join(sql.split())), param)
        data = res.fetchall()
        if len(data) == 0:
            sql = '''
                insert into cm_archieve.dangan
                (DangAnHao, ShenFenZheng, XingMing, XingBie, ChuShengRiQi,
                    YuTuiXiuRiQi, RenYuanLeiBie, CunDangRiQi, CunDangZhuangTai)
                values (:archieve_id, :identity, :name, :gender, :dob, :dor,
                    :cat, :arch_date, :arch_status)
            '''
            param = {'archieve_id': sh.cell(row, 3).value,
                'identity': sh.cell(row, 0).value,
                'name': sh.cell(row, 1).value,
                'gender': sh.cell(row, 2).value,
                'dob': dob,
                'dor': dor,
                'cat': sh.cell(row, 4).value,
                'arch_date': sh.cell(row, 5).value,
                'arch_status': sh.cell(row, 6).value}
        else:
            sql = '''
                update dangan
                set DangAnHao=:archieve_id, ShenFenZheng=:identity,
                    XingMing=:name, XingBie=:gender, ChuShengRiQi=:dob,
                    YuTuiXiuRiQi=:dor, RenYuanLeiBie=:cat,
                    CunDangRiQi=:arch_date, CunDangZhuangTai=:arch_status
                where id=:id
            '''
            param = {'archieve_id': sh.cell(row, 3).value,
                'identity': sh.cell(row, 0).value,
                'name': sh.cell(row, 1).value,
                'gender': sh.cell(row, 2).value,
                'dob': dob,
                'dor': dor,
                'cat': sh.cell(row, 4).value,
                'arch_date': sh.cell(row, 5).value,
                'arch_status': sh.cell(row, 6).value,
                'id': data[0].id}
        db_engine.execute(text(' '.join(sql.split())), param)
