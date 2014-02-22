# -*- coding=UTF-8 -*-

source_path = 'd:\\test1'
target_path = 'd:\\test2'

db_param = {
    'user': 'cmtech',
    'password': 'cmtech.1123',
    'host': '125.211.221.215',
    'database': 'cm_archieve',
}

def connect_db():
    import mysql.connector

    return mysql.connector.Connect(**db_param)


def close_db(cursor, cnx):
    cursor.close()
    cnx.close()


def insert_rec(archieve_id):
    sql = 'select id from dangan where danganhao=%(archieve_id)s'
    param = {
        archieve_id: archieve_id
    }
    cnx = conenct_db()
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    result = cursor.fetchall()
    print result


def rename_dir():
    import os

    for item in os.listdir(source_path):
        p = os.path.join(source_path, item)
        if os.path.isdir(p):
            name = item.split('-')[len(item.split('-')) - 1]
            print u'重命名:', p, '->', os.path.join(source_path, name)
            os.rename(p, os.path.join(source_path, name))


def import_files(path):
    import os

    for item in os.listdir(path):
        p = os.path.join(path, item)
        if os.path.isdir(p):
            print u'目录:', p
            import_files(p)
        else:
            print u'文件:', p


if __name__ == '__main__':
    rename_dir()
    import_files(path=source_path)