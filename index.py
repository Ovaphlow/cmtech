# -*- coding=UTF-8 -*-
from flask.views import MethodView

import globalvars


class Index(MethodView):
    def get(self):
        import mysql.connector
        from flask import redirect, render_template, session

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
        return render_template('index.html', data=data, User=session['user'])

    def post(self):
        import mysql.connector
        from flask import request, redirect

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
