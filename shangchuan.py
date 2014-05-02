# -*- coding=UTF-8 -*-

import os

from flask import session, request, render_template, redirect
from flask.views import MethodView
from werkzeug import secure_filename

from globalvars import connect_db, close_db, get_file_path, G_UPLOAD_PATH, \
    get_aid, check_path, check_ext, caozuo_jilu


class ShangChuan(MethodView):
    def get(self, rec_id):
        if not 'user_id' in session:
            return redirect('/login')
        cat = request.args.get('cat', '1')
        sql = '''
            SELECT * FROM dangan
            WHERE id=%s
        '''
        param = (rec_id,)
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if cursor.rowcount > 0:
            row = data[0]
        else:
            row = None
        close_db(cursor, cnx)
        fp = get_file_path(rec_id)
        lp = '/saomiao/%s' % (rec_id,)
        return render_template(
            'shangchuan.html',
            row = row,
            id = rec_id,
            filepath = fp,
            link = lp,
            cat = cat,
            User = session['user_name']
        )

    def post(self, rec_id):
        # print 'upload path:', G_UPLOAD_PATH
        # print 'headers', request.headers
        cat = request.args.get('cat', '1')
        # print 'id', id
        # print id, cat
        # print 'request.value', request.values
        aid = get_aid(rec_id)
        fp = '%s\\%s' % (G_UPLOAD_PATH, aid)
        check_path(fp)
        cnx = connect_db()
        cursor = cnx.cursor()
        for f in request.files.getlist('Filedata'):
            if f and check_ext(f.filename):
                fn = secure_filename(f.filename)
                fp = os.path.join(fp, fn)
                f.save(fp)
                sql = '''
                    INSERT INTO wenjian (id,aid,LeiBie,WenJianMing)
                    VALUES(0,%s,%s,%s)
                '''
                param = (rec_id, cat, fn)
                cursor.execute(sql, param)
                caozuo_jilu(session['user_id'], u'批量上传', rec_id)
        cnx.commit()
        close_db(cursor, cnx)
        return '[%s]上传完成' % (fn)
