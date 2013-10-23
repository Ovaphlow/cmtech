# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import render_template, request, redirect


def dytx_get():
    import time
    t = time.localtime()
    time_str = time.strftime('%Y-%m', t)
    sql = 'SELECT * FROM dangan WHERE YuTuiXiuRiQi LIKE "' + time_str + '%"'
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template('dytx.html', data=data)
