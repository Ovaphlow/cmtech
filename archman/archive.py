# -*- coding=UTF-8 -*-

import gl

from flask import redirect, render_template, session, request
from flask.views import MethodView
from sqlalchemy import text


class Archive(MethodView):
    def get(self):
        if not 'user' in session:
            return redirect('/')
        sql = '''
            select *
            from archive
            where id=:id
        '''
        param = {'id': request.args.get('id')}
        res = gl.db_engine.execute(text(' '.join(sql.split())), param)
        archive = res.fetchone()
        res.close()
        return render_template('archive/archive.html', User=session['user'],
            archive=archive)

    def post(self):
        id = request.form['id']
        sql = '''
            update archive
            set id_card=:id_card, name=:name, gender=:gender,
                birthday=:birthday, retire_date=:retire_date,
                female_cadre=:female, special_personnel=:special,
                transfer_out=:transfer
            where id=:id
        '''
        param = {'id': id,
            'id_card': request.form['id_card'],
            'name': request.form['name'],
            'gender': request.form['gender'],
            'birthday': request.form['birthday'],
            'retire_date': request.form['retire_date'],
            'female': request.form['female_cadre'],
            'special': request.form['special_personnel'],
            'transfer': request.form['transfer_out']}
        gl.db_engine.execute(text(' '.join(sql.split())), param)
        return redirect('/archive?id=%s' % id)
