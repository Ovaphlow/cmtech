# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import request, render_template, redirect

def get():
    return render_template('luru.boot.html')

def post():
    s, t = 0, 0
    if 'female' in request.form.getlist('check'):
        s = 1
    if 'stow' in request.form.getlist('check'):
        t = 1
    dob = '%s-%s-%s' % (
        request.form['dob-year'],
        request.form['dob-month'],
        request.form['dob-date']
    )
    dor = '%s-%s-%s' % (
        request.form['dor-year'],
        request.form['dor-month'],
        request.form['dor-date']
    )
    sql = (
        'INSERT INTO dangan '
        'VALUES('
        '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    )
    param = (
        0, request.form['aid'], request.form['idcard'],
        request.form['name'], request.form['gender'], dob,
        dor, '', '',
        '', s, t
    )
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    cnx.commit()
    aid = cursor.lastrowid
    return redirect('/saomiao/%s' % (aid))
