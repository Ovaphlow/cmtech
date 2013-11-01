# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import render_template, request, redirect, session


def get():
    if not 'id' in session:
        return redirect('/login')
    sql = 'SELECT * FROM dangan WHERE TeShuGongZhong=1'
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template('tsgz.html', data=data)


def post():
    pass