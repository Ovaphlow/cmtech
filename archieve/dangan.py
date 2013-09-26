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
    return render_template('dangan.boot.html', row=data[0])
