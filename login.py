# -*- coding=UTF-8 -*-
from flask.views import MethodView


class Login(MethodView):
    def get(self):
        from flask import render_template

        return render_template('login.html')

    def post(self):
        from flask import request, redirect, session
        import mysql.connector
        import globalvars

        zhang_hao = request.form['zhanghao']
        mi_ma = request.form['mima']
        cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cursor = cnx.cursor()
        sql = 'SELECT COUNT(*),id,ZhangHao FROM user WHERE ZhangHao=%s AND MiMa=%s'
        param = (zhang_hao, mi_ma)
        cursor.execute(sql, param)
        data = cursor.fetchall()
        #print 'count:', data[0][0], 'zhanghao:', data[0][1], 'mima:', data[0][2]
        if data[0][0] == 1:
            session['zhanghao'] = data[0][2]
            session['id'] = data[0][1]
            return redirect('/')
        else:
            return redirect('/login')
