# -*- coding=UTF-8 -*-

import globalvars

from flask import session, redirect, render_template, request
from flask.views import MethodView

from globalvars import idcard_convert, get_years, connect_db, close_db, \
    caozuo_jilu


class LuRu(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        _err = request.args.get('err', '0')
        if _err == '1':
            _err_message = u'档案号不能为空'
        elif _err == '2':
            _err_message = u'身份证不能为空'
        elif _err == '3':
            _err_message = u'姓名不能为空'
        elif _err == '4':
            _err_message = u'档案号或身份证号已存在'
        else:
            _err_message = None
        return render_template('luru.html',
            User=session['user_name'],
            error=_err_message
        )

    def post(self):
        _danganhao = request.form['aid']
        _idcard = request.form['idcard']
        _name = request.form['name']
        if not _danganhao:
            return redirect('/luru?err=1')
        if not _idcard:
            return redirect('/luru?err=2')
        if not _name:
            return redirect('/luru?err=3')
        s, t = 0, 0
        if 'female' in request.form.getlist('check'):
            s = 1
        if 'stow' in request.form.getlist('check'):
            t = 1
        if len(_idcard) == 15:
            idcard_18 = idcard_convert(request.form['idcard'])
        else:
            idcard_18 = _idcard
        dob = idcard_18[6:14]
        if int(idcard_18[16:17]) % 2 == 1:
            gender = u'男'
        else:
            gender = u'女'
        dob = '%s-%s-%s' % (dob[0:4], dob[4:6], dob[6:8])
        dor_y = dob[0:4]
        years = get_years(gender, t, s)
        dor = '%s-%s-%s' % (int(dor_y) + years, dob[5:7], dob[8:10])
        cnx = connect_db()
        cursor = cnx.cursor()
        sql = ('select count(*) '
            'from dangan '
            'where danganhao=%(archieve_id)s '
            'or shenfenzheng=%(idcard)s')
        param = {
            'archieve_id': _danganhao,
            'idcard': idcard_18
        }
        cursor.execute(sql, param)
        res = cursor.fetchall()
        if res[0][0] > 0:
            return redirect('/luru?err=4')
        sql = '''
            INSERT INTO dangan
            (DangAnHao,ShenFenZheng,XingMing,XingBie,ChuShengRiQi,
            YuTuiXiuRiQi,NvGuanLiGangWei,TeShuGongZhong)
            VALUES
            (%(archieve_id)s,%(idcard)s,%(name)s,%(gender)s, %(dob)s,
            %(dor)s, %(ngl)s, %(stow)s)
        '''
        param = {
            'archieve_id': _danganhao,
            'idcard': idcard_18,
            'name': _name,
            'gender': gender,
            'dob': dob,
            'dor': dor,
            'ngl': s,
            'stow': t
        }
        cursor.execute(sql, param)
        cnx.commit()
        rec_id = cursor.lastrowid
        close_db(cursor, cnx)
        caozuo_jilu(session['user_id'], u'添加档案信息', rec_id)
        return redirect('/saomiao/%s' % (rec_id))
