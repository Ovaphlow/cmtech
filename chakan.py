# -*- coding=UTF-8 -*-
from flask.views import MethodView


class ChaKan(MethodView):
    def get(self, pic_id):
        from flask import session, redirect, render_template
        import mysql.connector
        import globalvars

        if not 'id' in session:
            return redirect('/login')
        sql = '''
            SELECT wenjian.id,wenjian.aid,wenjian.wenjianming,dangan.danganhao
            FROM wenjian INNER JOIN dangan ON wenjian.aid=dangan.id
            WHERE wenjian.id=%s
        '''
        param = (pic_id,)
        cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        cursor.close()
        cnx.close()
        row = data[0]
        return render_template('chakan.html',
                               fs_root=globalvars.G_FILE_SERVER_ROOT,
                               aid=row[3],
                               row=row
        )

    def post(self, pic_id):
        from flask import redirect, request
        import mysql.connector
        import globalvars
        import os

        opr = request.form['operate']
        if opr == 'turn':
            sql = '''
                SELECT wenjian.id,wenjian.aid,wenjian.wenjianming,dangan.danganhao
                FROM wenjian INNER JOIN dangan ON wenjian.aid=dangan.id
                WHERE wenjian.id=%s
            '''
            param = (pic_id,)
            cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            cursor.close()
            cnx.close()
            row = data[0]
            ret = globalvars.turn_image('%s\%s\%s' % (globalvars.G_UPLOAD_PATH, row[3], row[2]))
        elif opr == 'delete':
            sql = '''
                SELECT wenjian.id,wenjian.aid,wenjian.wenjianming,dangan.danganhao
                FROM wenjian INNER JOIN dangan ON wenjian.aid=dangan.id
                WHERE wenjian.id=%s
            '''
            param = (pic_id,)
            cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            sql = 'DELETE FROM wenjian WHERE id=%s'
            param = (pic_id,)
            cursor.execute(sql, param)
            cnx.commit()
            cursor.close()
            cnx.close()
            row = data[0]
            fp = '%s\%s\%s' % (globalvars.G_UPLOAD_PATH, row[3], row[2])
            if os.path.isfile(fp):
                os.remove(fp)
        return redirect('/dangan/%s' % row[1])
