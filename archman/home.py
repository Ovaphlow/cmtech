# -*- coding=UTF-8 -*-

import gl

from flask import redirect, render_template, session, request
from flask.views import MethodView
from sqlalchemy import text


class Home(MethodView):
    def get(self):
        if not 'user' in session:
            return redirect('/login')
        return render_template('home.html', User=session['user'])

    def post(self):
        identity = request.form['identity']
        sql = '''
            select id
            from archive
            where id=:identity
            or id_card=:identity
        '''
        param = {'identity': identity}
        res = gl.db_engine.execute(text(' '.join(sql.split())), param)
        archive = res.fetchall()
        res.close()
        if len(archive) != 1:
            return redirect('/')
        return redirect('/archive?id=%s' % archive[0].id)


class Login(MethodView):
    def get(self):
        sql = '''
            select *
            from event_log
            order by id desc
            limit 10
        '''
        sql = ' '.join(sql.split())
        res = gl.db_engine.execute(text(sql))
        event = res.fetchall()
        res.close()
        return render_template('login.html', event=event)

    def post(self):
        acc = request.form['account']
        pwd = request.form['password']
        sql = '''
            select *
            from user
            where account=:acc
            and password=:pwd
        '''
        param = {'acc': acc,
            'pwd': pwd}
        res = gl.db_engine.execute(text(' '.join(sql.split())), param)
        data = res.fetchall()
        res.close()
        if len(data) != 1:
            return redirect('/login')
        session['user'] = {'id': data[0].id,
            'account': data[0].account,
            'name': data[0].name}
        session['auth'] = {'amend': data[0].auth_amend}
        return redirect('/')


class Logout(MethodView):
    def get(self):
        session.pop('user')
        session.pop('auth')
        return redirect('/login')
