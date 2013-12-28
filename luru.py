# -*- coding=UTF-8 -*-
from flask.views import MethodView


class LuRu(MethodView):
    def get(self):
        from flask import session, redirect, render_template, request

        if not 'user_id' in session:
            return redirect('/login')
        return render_template(
            'luru.html',
            User = session['user_name'],
            error = request.args.get('err')
        )

    def post(self):
        from flask import request, redirect, session
#         import mysql.connector
        import globalvars

        s, t = 0, 0
        if 'female' in request.form.getlist('check'):
            s = 1
        if 'stow' in request.form.getlist('check'):
            t = 1
        dob = request.form['idcard'][6:14]
        if int(request.form['idcard'][16:17]) % 2 == 1:
            gender = u'男'
        else:
            gender = u'女'
        dob = '%s-%s-%s' % (dob[0:4], dob[4:6], dob[6:8])
        dor_y = dob[0:4]
        years = globalvars.get_years(gender, t, s)
        dor = '%s-%s-%s' % (int(dor_y) + years, dob[5:7], dob[8:10])
        sql = '''
            INSERT INTO dangan
            VALUES(
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        param = (
            0, request.form['aid'], request.form['idcard'],
            request.form['name'], gender, dob,
            dor, '', '',
            '', s, t
        )
#         cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        cnx.commit()
        aid = cursor.lastrowid
#         cursor.close()
#         cnx.close()
        globalvars.close_db(cursor, cnx)
        globalvars.caozuo_jilu(session['user_id'], u'添加档案信息', aid)
        return redirect('/saomiao/%s' % (aid))
