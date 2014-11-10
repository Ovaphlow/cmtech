# -*- coding=UTF-8 -*-

import gl

from flask import redirect, render_template, session, request
from flask.views import MethodView
from sqlalchemy import text

from archman import app

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        if not 'user' in session:
            return redirect('/login')
        return 'hello world'
    identity = request.form['identity']
    sql = '''
        select id
        from archive
        where id=:identity
        or id_card=:identity
    '''
    param = {'identity': identity}
    res = gl.db_engine.execute(text(sql), param)
    archive = res.fetchall()
    res.close()
    if len(archive) != 1:
        return redirect('/')
    return redirect('/archive?id=%s' % archive[0].id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
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
    sql = '''
        select *
        from user
        where account=:acc
        and password=:pwd
    '''
    param = {'acc': request.form['account'],
        'pwd': request.form['password']}
    res = gl.db_engine.execute(text(sql), param)
    data = res.fetchall()
    res.close()
    if len(data) != 1:
        return redirect('/login')
    session['user'] = {'id': data[0].id,
        'account': data[0].account,
        'name': data[0].name}
    session['auth'] = {'amend': data[0].auth_amend}
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user')
    session.pop('auth')
    return redirect('/login')
