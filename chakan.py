# -*- coding=UTF-8 -*-
from flask.views import MethodView


class ChaKan(MethodView):
    def get(self, pic_id):
        from flask import session, redirect, render_template
        import globalvars

        if not 'user_id' in session:
            return redirect('/login')
        sql = '''
            SELECT wenjian.id,wenjian.aid,wenjian.wenjianming,dangan.danganhao
            FROM wenjian INNER JOIN dangan ON wenjian.aid=dangan.id
            WHERE wenjian.id=%s
        '''
        param = (pic_id,)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        globalvars.close_db(cursor, cnx)
        row = data[0]
        return render_template(
            'chakan.html',
            fs_root = globalvars.G_FILE_SERVER_ROOT,
            aid = row[3],
            row = row,
            User = session['user_name']
        )

    def post(self, pic_id):
        from flask import redirect, request
        import globalvars
        import os

        opr = request.form['operate']
        if opr == 'turn':
            sql = '''
                SELECT w.id,w.aid,w.wenjianming,d.danganhao
                FROM wenjian w INNER JOIN dangan d ON w.aid=d.id
                WHERE w.id=%s
            '''
            param = (pic_id,)
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            row = data[0]
            globalvars.turn_image(
                '%s\%s\%s' % \
                (globalvars.G_UPLOAD_PATH, row[3], row[2])
            )
        elif opr == 'delete':
            sql = '''
                SELECT w.id,w.aid,w.wenjianming,d.danganhao
                FROM wenjian w INNER JOIN dangan d ON w.aid=d.id
                WHERE w.id=%s
            '''
            param = (pic_id,)
            cnx = globalvars.connect_db
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            sql = 'DELETE FROM wenjian WHERE id=%s'
            param = (pic_id,)
            cursor.execute(sql, param)
            cnx.commit()
            row = data[0]
            fp = '%s\%s\%s' % (globalvars.G_UPLOAD_PATH, row[3], row[2])
            if os.path.isfile(fp):
                os.remove(fp)
        globalvars.close_db(cursor, cnx)
        return redirect('/dangan/%s' % row[1])
