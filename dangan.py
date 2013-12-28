# -*- coding=UTF-8 -*-
from flask.views import MethodView


class DangAn(MethodView):
    def get(self, aid):
        from flask import session, redirect, request, render_template
#         import mysql.connector
        import globalvars

        if not 'user_id' in session:
            return redirect('/login')
        cat = request.args.get('cat', '0')
        sql = 'SELECT * FROM dangan WHERE id=%s'
        param = (aid,)
#         cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        dob = data[0][5].split('-')
        dor = data[0][6].split('-')
        if cat == '0':
            sql = 'SELECT * FROM wenjian WHERE aid=%s'
            param = (aid,)
        else:
            sql = 'SELECT * FROM wenjian WHERE aid=%s AND LeiBie=%s'
            param = (aid, cat)
        cursor.execute(sql, param)
        data1 = cursor.fetchall()
#         cursor.close()
#         cnx.close()
        globalvars.close_db(cursor, cnx)
        lp1 = '/saomiao/%s' % (aid,)
        lp2 = '/luru/%s' % (aid,)
        return render_template(
            'dangan.html',
            id = aid,
            row = data[0],
            link1 = lp1,
            link2 = lp2,
            fs_root = globalvars.G_FILE_SERVER_ROOT,
            aid = globalvars.get_aid(aid),
            data1 = data1,
            dob = dob,
            dor = dor,
            cat = cat,
            User = session['user_name']
        )

    def post(self, aid):
        from flask import request, redirect, session
#         import mysql.connector
        import globalvars

        idcard = request.form['shenfenzheng']
        name = request.form['xingming']
        if int(idcard[16:17]) % 2 == 1:
            gender = u'男'
        else:
            gender = u'女'
        s, t = 0, 0
        if 'female' in request.form.getlist('check'):
            s = 1
        if 'stow' in request.form.getlist('check'):
            t = 1
        dob = '%s-%s-%s' % (
            request.form['dob-year'],
            request.form['dob-month'],
            request.form['dob-date']
        )
        dor = '%s-%s-%s' % (
            request.form['dor-year'],
            request.form['dor-month'],
            request.form['dor-date']
        )
        sql = '''
            UPDATE dangan
            SET
            ChuShengRiQi=%s,YuTuiXiuRiQi=%s,NvGuanLiGangWei=%s,
            TeShuGongZhong=%s,XingMing=%s,ShenFenZheng=%s,
            XingBie=%s
            WHERE id=%s
        '''
        param = (dob, dor, s, t, name, idcard, gender, aid)
#         cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        cnx.commit()
#         cursor.close()
#         cnx.close()
        globalvars.close_db(cursor, cnx)
        globalvars.caozuo_jilu(session['user_id'], u'修改档案信息', id)
        return redirect('/dangan/%s' % (aid))
