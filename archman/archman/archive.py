# -*- coding=UTF-8 -*-

import time
import os

import gl

from flask import redirect, render_template, session, request
from flask.views import MethodView
from sqlalchemy import text
from werkzeug import secure_filename

from archman import app


@app.route('/archive/<archive>', methods=['POST', 'GET'])
def archive(archive):
    if request.method == 'POST':
        sql = '''
update archive
set identity=:identity, name=:name, gender=:gender, birthday=:birthday,
    retire_date=:retire_date, female_cadre=:female_cadre,
    special_personnel=:special_personnel
where archive=:archive
        '''
        param = {
            'identity': request.form['identity'],
            'name': request.form['name'],
            'gender': request.form['gender'],
            'birthday': request.form['birthday'],
            'retire_date': request.form['retire_date'],
            'female_cadre': request.form['female_cadre'],
            'special_personnel': request.form['special_personnel'],
            'archive': archive
        }
        gl.db_engine.execute(text(sql), param)
        return redirect('/archive/%s' % archive)

    sql = '''
select *
from archive
where archive=:archive
    '''
    param = {'archive': archive}
    res = gl.db_engine.execute(text(sql), param)
    archive = res.fetchone()
    return render_template('archive/archive.html', User=session['user'],
        archive=archive)


@app.route('/archive/append', methods=['POST'])
def append():
    sql = '''
select *
from archive
where archive=:archive
    '''
    param = {'archive': request.form['g_archive']}
    res = gl.db_engine.execute(text(sql), param)
    print(res.rowcount)
    if res.rowcount > 0:
        return redirect('/')

    return redirect('/archive/%s' % request.form['g_archive'])


@app.route('/archive/<archive>/upload', methods=['POST'])
def upload(archive):
    f = request.files['Filedata']
    file_name = secure_filename(f.filename)
    file_ext = file_name.rsplit('.', 1)[1]
    print(gl.get_timestr())
    file_name = '%s.%s' % (time.time(), file_ext)
    file_path = os.path.join(app.config['NGINX_PATH'],
        app.config['FILE_DIR'], archive, file_name)
    f.save(file_path)
    sql = '''
insert
into file
    (archive, file_name)
values
    (:archive, :file_name)
    '''
    param = {
        'archive': archive,
        'file_name': file_name
    }
    gl.db_engine.execute(text(sql), param)
    return 'Success.'


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
        param = {'id': archive_id}
        res = gl.db_engine.execute(text(sql), param)
        archive = res.fetchone()
        sql = '''
select *
from file
where archive_id=:archive_id
        '''
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
        param = {
            'id': id,
            'id_card': request.form['id_card'],
            'name': request.form['name'],
            'gender': request.form['gender'],
            'birthday': request.form['birthday'],
            'retire_date': request.form['retire_date'],
            'female': request.form['female_cadre'],
            'special': request.form['special_personnel'],
            'transfer': request.form['transfer_out']
        }
        gl.db_engine.execute(text(sql), param)
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
        param = {
            'archive_id': archive_id,
            'file_name': file_name
        }
        gl.db_engine.execute(text(sql), param)
        return '1'
