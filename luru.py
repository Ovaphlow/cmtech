# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import request, render_template, redirect, session, escape


def get():
    if not 'id' in session:
        return redirect('/login')
    return render_template('luru.html')


def post():
    s, t = 0, 0
    if 'female' in request.form.getlist('check'):
        s = 1
    if 'stow' in request.form.getlist('check'):
        t = 1
    dob = request.form['idcard'][6:14]
    if int(request.form['idcard'][16:17]) % 2 == 1:
        gender = u'男'
    else:
        gender = u'女'
    dob = '%s-%s-%s' % (dob[0:4], dob[4:6], dob[6:8])
    dor_y = dob[0:4]
    years = globalvars.get_years(gender, t, s)
    dor = '%s-%s-%s' % (int(dor_y) + years, dob[5:7], dob[8:10])
    sql = '''
        INSERT INTO dangan
        VALUES(
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    param = (
        0, request.form['aid'], request.form['idcard'],
        request.form['name'], gender, dob,
        dor, '', '',
        '', s, t
    )
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    cnx.commit()
    aid = cursor.lastrowid
    cursor.close()
    cnx.close()
    globalvars.caozuo_jilu(escape(session['id']), u'添加档案信息', aid)
    return redirect('/saomiao/%s' % (aid))
