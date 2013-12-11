# -*- coding=UTF-8 -*-
from flask.views import MethodView


class Index(MethodView):
    def get(self):
        import mysql.connector
        from flask import redirect, render_template, session
        import globalvars

        if not 'id' in session:
            return redirect('/login')
        sql = (
            'SELECT * FROM update_log '
            'ORDER BY id DESC'
        )
        cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        sql = '''
            SELECT COUNT(*) FROM dangan
            UNION
            SELECT COUNT(*) FROM (
                SELECT d.id
                FROM dangan d
                INNER JOIN wenjian w
                ON d.id=w.aid
                GROUP BY d.id
            ) AS a
            UNION
            SELECT COUNT(*) FROM wenjian
        '''
        cursor.execute(sql)
        data_count = cursor.fetchall()
        cursor.close()
        cnx.close()
        return render_template('index.html',
                               data=data,
                               User=session['user'],
                               data_count = data_count
        )

    def post(self):
        import mysql.connector
        from flask import request, redirect
        import globalvars

        sql = 'SELECT id FROM dangan WHERE DangAnHao=%s OR ShenFenZheng=%s'
        param = (request.form['id'], request.form['id'])
        cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if cursor.rowcount == 0:
            return redirect('/luru')
        else:
            return redirect('/dangan/' + str(data[0][0]))
