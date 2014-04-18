# -*- coding=UTF-8 -*-

# 修改操作记录表中neirong字段的数据
# 由图片地址改为档案编号

import mysql.connector


cnx_param = {
    'user': 'cmtech',
    'password': 'cmtech.1123',
    'host': '125.211.221.215',
    'database': 'cm_archieve',
}


def open_db():
    return mysql.connector.Connect(**cnx_param)


def close_db(cursor, cnx):
    cursor.close()
    cnx.close()


def get_log_data():
    sql = '''
        select *
        from cm_archieve.caozuo_jilu
        where caozuo="上传图片"
    '''
    cnx = open_db()
    cursor = cnx.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    close_db(cursor, cnx)
    return res


def get_rec_id(danganhao):
    sql = 'select id FROM dangan WHERE danganhao=%(danganhao)s'
    param = {'danganhao': danganhao}
    cnx = open_db()
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    res = cursor.fetchall()
    close_db(cursor, cnx)
    return res[0][0]


def modify_log():
    res = get_log_data()
    cnx = open_db()
    cursor = cnx.cursor()

    for row in res:
        sql = '''
            update caozuo_jilu
            set Neirong=%(neirong)s
            where id=%(id)s
        '''
        param = {
            'id': row[0]
        }
        try:
            _nr = row[3].split('\\')
            if len(_nr) == 1:
                continue
            _archieve_id = _nr[len(_nr) - 2]
            _rec_id = get_rec_id(_archieve_id)
            param['neirong'] = _rec_id

            cursor.execute(sql, param)
        except:
            print 'err:', row[0]
            continue
        else:
            pass
    cnx.commit()
    close_db(cursor, cnx)


if __name__ == '__main__':
    modify_log()