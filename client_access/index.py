# -*- coding=UTF-8 -*-
from flask.views import MethodView


class Index(MethodView):
    def get(self):
        from flask import render_template, session, request

        err = request.args.get('err', 0)
        if err == '1':
            return render_template('index.html',
                error_message=u'身份证输入错误')
        return render_template('index.html')

    def post(self):
        from flask import redirect, request, session
        import g_vars
        import datetime

        now_date = datetime.datetime.now().strftime('%Y-%m-%d')
        sql = '''
            SELECT COUNT(*) FROM access_code
            WHERE archieve_id=%(archieve_id)s AND date=%(date)s
        '''
        param = {
            'archieve_id': request.form['idcard'],
            'date': now_date
        }
        cnx = g_vars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        if result[0][0] >= 1:
            session['idcard'] = request.form['idcard']
            return redirect('/code')
        else:
            return redirect('/?err=1')


class Code(MethodView):
    def get(self):
        from flask import render_template, session, request

        err = request.args.get('err', 0)
        if err == '1':
            return render_template('code.html',
                error_message=u'密码输入错误')
        elif err == '2':
            return render_template('code.html',
                error_message=u'无可用密码，请到柜台查询。')
        return render_template('code.html')

    def post(self):
        from flask import session, request, redirect
        from g_vars import connect_db, close_db
        import datetime

        now_date = datetime.datetime.now().strftime('%Y-%m-%d')
        sql = '''
            select
                *
            from
                access_code
            where
                archieve_id=%(archieve_id)s
                and
                date=%(date)s
            order by
                id
                desc
            limit 1
        '''
        param = {
            'archieve_id': session['idcard'],
            'date': now_date
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        if result == None:
            return redirect('/code?err=2')
        if result[0][2] != request.form['code']:
            return redirect('/code?err=1')
        session['code'] = request.form['code']
        return redirect('/archieve')


class Logout(MethodView):
    def get(self):
        from flask import session, redirect

        session.pop('idcard', None)
        session.pop('code', None)
        return redirect('/')