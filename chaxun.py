# -*- coding=UTF-8 -*-
from flask.views import MethodView


class ChaXun(MethodView):
    def get(self):
        from flask import render_template, session, redirect
        if not 'user_id' in session:
            return redirect('/login')

        return render_template('chaxun.html', User = session['user_name'])

    def post(self):
        from flask import request, render_template, session
#         import mysql.connector
        import globalvars
        import sys

        reload(sys)
        sys.setdefaultencoding('utf-8')
        aid = request.form['DangAnHao']
        idcard = request.form['ShenFenZheng']
        name = request.form['XingMing']
        gender = request.form['XingBie']
        sql = 'SELECT * FROM dangan WHERE XingBie="'
        sql = '%s%s"' % (sql, gender)
        if aid != '':
            sql = '%s AND DangAnHao LIKE "%s%s%s"' % (sql, '%', aid, '%')
        if idcard != '':
            sql = '%s AND ShenFenZheng LIKE "%s%s%s"' % (sql, '%', idcard, '%')
        if name != '':
            sql = '%s AND XingMing LIKE "%s%s%s"' % (sql, '%', name, '%')
        sql = '%s LIMIT 100' % (sql,)
#         print sql
#         param = (gender,)
#         cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        globalvars.close_db(cursor, cnx)
        return render_template('chaxun.html', data = data, User = session['user_name'])


class DangYueTuiXiu(MethodView):
    def get(self):
        import time
        import globalvars
        from flask import render_template, redirect, session

        if not 'user_id' in session:
            return redirect('/login')

        t = time.localtime()
        time_str = time.strftime('%Y-%m', t)
        sql = 'SELECT * FROM dangan WHERE YuTuiXiuRiQi LIKE "' + time_str + '%"'
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        globalvars.close_db(cursor, cnx)
        return render_template(
            'dytx.html',
            data = data,
            User = session['user_name']
        )

    def post(self):
        import globalvars
        from flask import render_template, redirect, session, request

        if not 'user_id' in session:
            return redirect('/login')
        d = '%s-%s' % (request.form['year'], request.form['month'])
        sql = 'SELECT * FROM dangan WHERE YuTuiXiuRiQi LIKE "' + d + '%"'
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        globalvars.close_db(cursor, cnx)
        return render_template(
            'dytx.html',
            data = result,
            user = session['user_name']
        )


class TeShuGongZhong(MethodView):
    def get(self):
        from flask import render_template, redirect, session
#         import mysql.connector
        import globalvars

        if not 'user_id' in session:
            return redirect('/login')
        sql = 'SELECT * FROM dangan WHERE TeShuGongZhong=1'
#         cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        globalvars.close_db(cursor, cnx)
        return render_template(
            'tsgz.html',
            data = data,
            User = session['user_name']
        )


class NvGuanLiGangWei(MethodView):
    def get(self):
        import globalvars
        from flask import render_template, redirect, session

        if not 'user_id' in session:
            return redirect('/login')
        sql = 'SELECT * FROM dangan WHERE NvGuanLiGangWei=1'
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        globalvars.close_db(cursor, cnx)
        return render_template(
            'nglgw.html',
            data = data,
            User = session['user_name']
        )
