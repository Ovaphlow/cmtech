# -*- coding=UTF-8 -*-
from flask.views import MethodView


class XiuGaiMiMa(MethodView):
    def get(self):
        from flask import render_template, session

        return render_template('xgmm.html', User=session['user'])

    def post(self):
        from flask import redirect, request, session
        import mysql.connector
        import globalvars

        jiumima = request.form['jiumima']
        xinmima = request.form['xinmima']
        xinmima2 = request.form['xinmima2']
        if xinmima != xinmima2:
            return redirect('/xgmm')
        sql = 'SELECT * FROM user WHERE id=%s'
        param = (session['id'],)
        cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if jiumima != data[0][2]:
            return redirect('/xgmm')
        sql = '''
            UPDATE user
            SET MiMa=%s
            WHERE id=%s
        '''
        param = (xinmima, session['id'])
        cursor.execute(sql, param)
        cnx.commit()
        cursor.close()
        cnx.close()
        return redirect('/')