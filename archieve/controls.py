# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
import os
from flask import request, redirect
from werkzeug import secure_filename

def _shangchuan():
    if request.method == 'POST':
        file_list = []
        #cnx = mysql.connector.connect(**globalvars.cnx_cfg)
        #cursor = cnx.cursor()
        files_list = request.files.getlist('file1')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        print 'fl1:', globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file2')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        print 'fl2:', globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file3')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        print 'fl3:', globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file4')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        print 'fl4:', globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file5')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        print 'fl5:', globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file6')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        print 'fl6:', globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file7')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        print 'fl7:', globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file8')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        print 'fl8;', globalvars.join_file_name(';', file_list)
        file_list = []
        files_list = request.files.getlist('file9')
        for f in files_list:
            if f and globalvars.check_ext(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
                file_list.append(filename)
        print 'fl9:', globalvars.join_file_name(';', file_list)
        return redirect('/')
