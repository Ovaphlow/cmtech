# -*- coding=UTF-8 -*-
from flask.views import MethodView


class Index(MethodView):
    def get(self):
        import mysql.connector
        from flask import redirect, render_template, session
        import globalvars

        if not 'user_id' in session:
            return redirect('/login')
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
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data_count = cursor.fetchall()
        sql = '''
            select
                caozuo, count(*)
            from
                caozuo_jilu
            where
                yh_id=%(user_id)s
            group by
                caozuo
        '''
        param = {'user_id': session['user_id']}
        cursor.execute(sql, param)
        result = cursor.fetchall()
        globalvars.close_db(cursor, cnx)
        opr_count1 = 0
        opr_count2 = 0
        opr_count3 = 0
        opr_count4 = 0
        for row in result:
            if row[0] == u'添加档案信息':
                opr_count1 = row[1]
            elif row[0] == u'修改档案信息':
                opr_count2 = row[1]
            elif row[0] == u'上传图片':
                opr_count3 = row[1]
            elif row[0] == u'批量上传':
                opr_count4 = row[1]
        return render_template(
            'index.html',
            User = session['user_name'],
            data_count = data_count,
            opr_count1 = opr_count1,
            opr_count2 = opr_count2,
            opr_count3 = opr_count3,
            opr_count4 = opr_count4,
        )

    def post(self):
        from flask import request, redirect
        import globalvars

        sql = 'SELECT id FROM dangan WHERE DangAnHao=%s OR ShenFenZheng=%s'
        param = (request.form['id'], request.form['id'])
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if cursor.rowcount == 0:
            return redirect('/luru')
        else:
            return redirect('/dangan/' + str(data[0][0]))


class Login(MethodView):
    def get(self):
        from flask import render_template

        return render_template('login.html')

    def post(self):
        from flask import request, redirect, session
        import globalvars

        zhang_hao = request.form['zhanghao']
        mi_ma = request.form['mima']
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        sql = 'SELECT COUNT(*),id,MingCheng FROM user WHERE ZhangHao=%s AND MiMa=%s'
        param = (zhang_hao, mi_ma)
        cursor.execute(sql, param)
        data = cursor.fetchall()
        globalvars.close_db(cursor, cnx)
        if data[0][0] == 1:
            session['user_name'] = data[0][2]
            session['user_id'] = data[0][1]
            return redirect('/')
        else:
            return redirect('/login')


class Logout(MethodView):
    def get(self):
        from flask import session, redirect

        session.pop('user_id', None)
        session.pop('user_name', None)
        return redirect('/login')
