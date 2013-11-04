# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import render_template, request, redirect, session

def get(id):
    if not 'id' in session:
        return redirect('/login')
    cat = request.args.get('cat', '0')
    sql = 'SELECT * FROM dangan WHERE id=%s'
    param = (id,)
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchall()
    dob = data[0][5].split('-')
    dor = data[0][6].split('-')
    if cat == '0':
        sql = 'SELECT * FROM wenjian WHERE aid=%s'
        param = (id,)
    else:
        sql = 'SELECT * FROM wenjian WHERE aid=%s AND LeiBie=%s'
        param = (id, cat)
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    cursor.close()
    cnx.close()
    lp1 = '/saomiao/%s' % (id,)
    lp2 = '/luru/%s' % (id,)
    return render_template('dangan.boot.html',
        id = id,
        row = data[0],
        link1 = lp1,
        link2 = lp2,
        fs_root = globalvars.G_FILE_SERVER_ROOT,
        aid = globalvars.get_aid(id),
        data1 = data1,
        dob = dob,
        dor = dor,
        cat = cat
    )

def post(id):
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
    sql = '''
        UPDATE dangan
        SET
        ChuShengRiQi=%s,YuTuiXiuRiQi=%s,NvGuanLiGangWei=%s,TeShuGongZhong=%s
        WHERE id=%s
    '''
    param = (dob, dor, s, t, id)
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    cnx.commit()
    cursor.close()
    cnx.close()
    #aid = cursor.lastrowid
    return redirect('/dangan/%s' % (id))
