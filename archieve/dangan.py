# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import render_template

def get(id):
    sql = 'SELECT * FROM dangan WHERE id=%s'
    param = (id,)
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchall()
    sql = 'SELECT * FROM wenjian WHERE id=%s'
    param = (id,)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    cursor.close()
    cnx.close()
    row1 = data1[0]
    strlist = []
    for i in range(1, 10):
        if not row1[i] == None:
            strlist_t = row1[i].split(';')
            strlist.extend(strlist_t)
    while '' in strlist:
        strlist.remove('')
    lp = '/shangchuan/%s' % (id,)
    return render_template('dangan.boot.html',
        row = data[0],
        link = lp,
        fs_root = globalvars.G_FILE_SERVER_ROOT,
        filelist = strlist,
        aid = globalvars.get_aid(id)
    )
