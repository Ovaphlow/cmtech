# -*- coding=UTF-8 -*-
from flask.views import MethodView


class Index(MethodView):
    def get(self):
        from flask import render_template, session
        return render_template('index.html')

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
            print('success:', result[0][0])
            session['idcard'] = request.form['idcard']
            return redirect('/code')
        else:
            print('err:', result[0][0])
            return redirect('/')


class Code(MethodView):
    def get(self):
        from flask import session, render_template
        print(session['idcard'])
        return render_template('code.html')

    def post(self):
        from flask import session, request, render_template
        print(session['idcard'])
        print(request.form['code'])
        return render_template('code.html')
