# -*- coding=UTF-8 -*-
import globalvars
from flask import request, render_template, redirect
from werkzeug import secure_filename
import mysql.connector


def get(id):
    url_root = request.url_root
    sql = (
        'SELECT * FROM dangan '
        'WHERE id=%s'
    )
    param = (
        id,
    )
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if cursor.rowcount > 0:
        row = data[0]
    else:
        row = None
    cursor.close()
    cnx.close()
    fp = globalvars.get_file_path(id)
    return render_template('saomiao.html', filepath=fp, row=row, id=id,
        url_root=url_root
    )


def post(id):
    #print request.data
    import os
    p = globalvars.get_file_path1(id)
    with open('d:\\11231.jpg', 'wb') as f:
        f.write(request.data)
    f.close()
    return 'Received'
