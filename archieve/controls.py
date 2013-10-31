# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
import os
from flask import request, redirect, jsonify
from werkzeug import secure_filename
import datetime


def upload_image_file():
    id = request.args.get('id', '')
    cat = request.args.get('cat', '')
    #print 'request.files:', request.files
    #print 'request.value:', request.values
    #print 'request.files[]', request.files['Filedata']
    aid = globalvars.get_aid(id)
    fp = '%s\\%s' % (globalvars.G_UPLOAD_PATH, aid)
    globalvars.check_path(fp)
    file_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    file_name = '%s.jpg' % (file_time)
    fp = '%s\\%s' % (fp, file_name)
    with open(fp, 'wb') as f:
        f.write(request.data)
    f.close()
    sql = '''
        INSERT INTO wenjian
        (aid, LeiBie, WenJianMing)
        VALUES(%s, %s, %s)
    '''
    param = (id, cat, file_name)
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    cnx.commit()
    cursor.close()
    cnx.close()
    globalvars.rotate_image(fp)
    return '完成'
