# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import request, render_template
from werkzeug import secure_filename

def get(id):
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
    return render_template('shangchuan.boot.html', row = row, id = id)
