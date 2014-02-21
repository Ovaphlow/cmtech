# -*- coding=UTF-8 -*-

from flask.views import MethodView


class ShangChuan(MethodView):
    def get(self, rec_id):
        from flask import session, request, render_template, redirect
        import globalvars

        if not 'user_id' in session:
            return redirect('/login')
        cat = request.args.get('cat', '1')
        sql = '''
            SELECT * FROM dangan
            WHERE id=%s
        '''
        param = (rec_id,)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if cursor.rowcount > 0:
            row = data[0]
        else:
            row = None
        globalvars.close_db(cursor, cnx)
        fp = globalvars.get_file_path(rec_id)
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
        from flask import request, session
        from werkzeug import secure_filename
        import os
        import globalvars
        # print 'upload path:', globalvars.G_UPLOAD_PATH
        # print 'headers', request.headers
        cat = request.args.get('cat', '1')
        # print 'id', id
        # print id, cat
        # print 'request.value', request.values
        aid = globalvars.get_aid(rec_id)
        fp = '%s\\%s' % (globalvars.G_UPLOAD_PATH, aid)
        globalvars.check_path(fp)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        for f in request.files.getlist('Filedata'):
            if f and globalvars.check_ext(f.filename):
                fn = secure_filename(f.filename)
                fp = os.path.join(fp, fn)
                f.save(fp)
                sql = '''
                    INSERT INTO wenjian (id,aid,LeiBie,WenJianMing)
                    VALUES(0,%s,%s,%s)
                '''
                param = (rec_id, cat, fn)
                cursor.execute(sql, param)
                globalvars.caozuo_jilu(session['user_id'], u'批量上传', fn)
        cnx.commit()
        globalvars.close_db(cursor, cnx)
        return '[%s]上传完成' % (fn)
