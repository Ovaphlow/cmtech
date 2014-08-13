# -*- coding=UTF-8 -*-

import datetime
import os
import shutil
import sys

from sqlalchemy import text, create_engine

cnx = {'user': 'root',
    'password': 'dsdfjk',
    'host': '127.0.0.1',
    'database': 'cm_archieve'}

db_engine = create_engine('mysql+mysqlconnector://%s:%s@%s/%s' % \
    (cnx['user'], cnx['password'], cnx['host'], cnx['database']),
    pool_recycle=900, pool_size=1)

# source_path = 'd:\\srcode\\cmtech-archieve\\misc\\source'
source_path = os.path.join(os.getcwd(), 'source')
# target_path = 'd:\\srcode\\cmtech-archieve\\misc\\target'
target_path = 'e:\\cmtech-archieve\\static\\upload'
path_divider = '\\'


def insert_rec(archieve_id):
    sql = '''
        select id from dangan where danganhao=:archieve_id
    '''
    param = {archieve_id: archieve_id}
    cnx = conenct_db()
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    result = cursor.fetchall()
    print result


def rename_dir():
    for item in os.listdir(source_path):
        p = os.path.join(source_path, item)
        if os.path.isdir(p):
            name = item.split('-')[len(item.split('-')) - 1]
            os.rename(p, os.path.join(source_path, name))


def copy_files(path):
    for item in os.listdir(path):
        p = os.path.join(path, item)
        if os.path.isdir(p):
            t = os.path.join(target_path, item)
            if not os.path.exists(t):
                os.mkdir(t)
            # print 'Working in directory:', p
            copy_files(p)
        else:
            dir_name = os.path.split(p)[0].split(path_divider)
            dir_name = dir_name[len(dir_name) - 1]
            time = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            file_name = '%s.%s' % (time, item.split('.')[-1])
            t = os.path.join(target_path, dir_name, file_name)
            if os.path.isfile(t):
                print 'Exists file:', t
                continue
            shutil.copyfile(p, t)
            sql = '''
                select id from dangan where danganhao=:archieve_id
            '''
            param = {'archieve_id': dir_name}
            res = db_engine.execute(text(' '.join(sql.split())), param)
            data = res.fetchall()
            if len(data) == 0:
                sql = '''
                    insert into dangan
                        (danganhao)
                    values
                        (:archieve_id)
                '''
                param = {'archieve_id': dir_name}
                db_engine.execute(text(' '.join(sql.split())), param)
            else:
                sql = '''
                    insert into wenjian
                      (aid, Leibie, WenJianMing, client_access)
                    values
                      (:archieve_id, :cat, :file_name, :client_access)
                '''
                param = {'archieve_id': data[0].id,
                    'cat': 9,
                    'file_name': file_name,
                    'client_access': 0}
                db_engine.execute(text(' '.join(sql.split())), param)
            res.close()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    copy_files(source_path)
