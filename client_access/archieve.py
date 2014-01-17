# -*- coding=UTF-8 -*-
from flask.views import MethodView


class Archieve(MethodView):
    def get(self):
        from flask import render_template, session
        import g_vars

        sql = '''
            SELECT ShenFenZheng,XingMing,YuTuiXiuRiQi
            FROM dangan
            WHERE ShenFenZheng=%(idcard)s
        '''
        param = {
            'idcard': session['idcard']
        }
        cnx = g_vars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        g_vars.close_db(cursor, cnx)
        return render_template(
            'archieve.html',
            row = result[0],
        )

    def post(self):
        from flask import redirect, request, session
        import g_vars

        sql = '''
            SELECT COUNT(*) FROM access_code
            WHERE archieve_id=%s AND date=%s
        '''
        param = (request.form['idcard'], '2014-01-06')
        cnx = g_vars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        if result[0][0] == 1:
            session['idcard'] = request.form['idcard']
            return redirect('/code')
        else:
            return redirect('/')
