# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
import os
from flask import request, redirect
from werkzeug import secure_filename

def _shangchuan(id):
    if request.method == 'POST':
        file_list = []
        files_list = request.files.getlist('file1')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        fl1 = globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file2')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        fl2 = globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file3')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        fl3 = globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file4')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        fl4 = globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file5')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        fl5 = globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file6')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        fl6 = globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file7')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        fl7 = globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file8')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        fl8 = globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file9')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        fl9 = globalvars.join_file_name(';', file_list)
        sql = 'SELECT COUNT(*) FROM wenjian WHERE id=%s'
        param = (id, )
        cnx = mysql.connector.connect(**globalvars.cnx_cfg)
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if data[0][0] == 0:
            sql = (
                'INSERT INTO wenjian '
                'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            )
            param = (id, fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9)
            cursor.execute(sql, param)
        else:
            sql = (
                'UPDATE wenjian '
                'SET '
                'cat_1=%s,cat_2=%s,cat_2=%s,cat_2=%s,cat_2=%s,cat_2=%s,'
                'cat_2=%s,cat_2=%s,cat_2=%s '
                'WHERE id=%s'
            )
            param = (fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9, id)
            cursor.execute(sql, param)
        cnx.commit()
        return redirect('/')
