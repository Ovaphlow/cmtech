# -*- coding=UTF-8 -*-

import datetime
import os

import gl
import settings

from flask import redirect, render_template, session, request
from flask.views import MethodView
from sqlalchemy import text
from werkzeug import secure_filename


class Archive(MethodView):
    def get(self):
        if not 'user' in session:
            return redirect('/')
        archive_id = request.args.get('id')
        sql = '''
            select *
            from archive
            where id=:id
        '''
        sql = ' '.join(sql.split())
        param = {'id': archive_id}
        res = gl.db_engine.execute(text(sql), param)
        archive = res.fetchone()
        sql = '''
            select *
            from file
            where archive_id=:archive_id
        '''
        sql = ' '.join(sql.split())
        param = {'archive_id': archive_id}
        res = gl.db_engine.execute(text(sql), param)
        file = res.fetchall()
        res.close()
        return render_template('archive/archive.html', User=session['user'],
            archive=archive, url_root=request.url_root, file=file)

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


class Upload(MethodView):
    def post(self):
        category = request.args.get('category')
        archive_id = request.args.get('archive_id')
        path = os.path.join(settings.nginx_path, settings.FILE_DIR, archive_id)
        f = request.files['Filedata']
        file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        file_name = '%s%s' % (file_name, settings.FILE_EXT)
        f.save(os.path.join(path, file_name))
        sql = '''
            insert into file
            (archive_id, file_name)
            values
            (:archive_id, :file_name)
        '''
        sql = ' '.join(sql.split())
        param = {'archive_id': archive_id,
            'file_name': file_name}
        gl.db_engine.execute(text(sql), param)
        return '1'
