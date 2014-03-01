# -*- coding=UTF-8 -*-

source_path = 'd:\\other_scanner'
target_path = 'd:\\cmtech-archieve\\static\\upload'
backup_path = 'd:\\backup_path'
path_divider = '\\'

db_param = {
    'user': 'root',
    'password': 'dsdfjk',
    'host': '127.0.0.1',
    'database': 'cm_archieve',
}

def open_db():
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
            os.rename(p, os.path.join(source_path, name))


def copy_files(path):
    import os
    import shutil

    for item in os.listdir(path):
        p = os.path.join(path, item)
        if os.path.isdir(p):
            t = os.path.join(target_path, item)
            if os.path.exists(t):
                print 'Exists directory:', t
                continue
            os.mkdir(t)
            print 'Working in directory:', p
            copy_files(p)
        else:
            dir_name = os.path.split(p)[0].split(path_divider)
            dir_name = dir_name[len(dir_name) - 1]
            t = os.path.join(target_path, dir_name, item)
            if os.path.isfile(t):
                print 'Exists file:', t
                continue
            shutil.copyfile(p, t)
            sql = ('select id from dangan where danganhao=%(archieve_id)s')
            param = {'archieve_id': dir_name}
            cnx = open_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            result = cursor.fetchall()
            if len(result) == 0:
                print 'No archieve #', dir_name, 'exists'
                b = os.path.join(backup_path, dir_name)
                if not os.path.exists(b):
                    os.mkdir(b)
                shutil.copyfile(p, os.path.join(backup_path, dir_name, item))
                continue
            sql = ('insert into wenjian '
                '(aid, Leibie, WenJianMing, client_access) '
                'values '
                '(%(archieve_id)s,'
                '%(cat)s,'
                '%(file_name)s,'
                '%(client_access)s)')
            param = {
                'archieve_id': result[0][0],
                'cat': 9,
                'file_name': item,
                'client_access': 0
            }
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)

if __name__ == '__main__':
    rename_dir()
    copy_files(source_path)