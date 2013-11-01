# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import request, redirect, render_template, session, escape


def get():
    if not 'id' in session:
        return redirect('/login')
    sql = (
        'SELECT * FROM update_log '
        'ORDER BY id DESC'
    )
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    cnx.close()
    return render_template('index.boot.html', data=data)


def post():
    sql = 'SELECT id FROM dangan WHERE DangAnHao=%s OR ShenFenZheng=%s'
    param = (request.form['id'], request.form['id'])
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if cursor.rowcount == 0:
        return redirect('/luru')
    else:
        return redirect('/dangan/' + str(data[0][0]))
