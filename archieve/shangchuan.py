# -*- coding=UTF-8 -*-

import os

import xlrd

from flask import session, request, render_template, redirect
from flask.views import MethodView
from sqlalchemy import text
from werkzeug import secure_filename

from globalvars import *


def import_xls(file_path):
    xls = xlrd.open_workbook(file_path, 'rb')
    sh = xls.sheets()[0]
    for row in range(1, sh.nrows):
        if sh.cell(row, 6).value != u'已调入':
            continue
        dob = sh.cell(row, 0).value
        dob = dob[6:14]
        dob = '%s-%s-%s' % (dob[0:4], dob[4:6], dob[6:8])
        dor_y = dob[0:4]
        if sh.cell(row, 2).value == u'男':
            dor = '%s-%s-%s' % (int(dor_y) + 60, dob[5:7], dob[8:10])
        else:
            dor = '%s-%s-%s' % (int(dor_y) + 50, dob[5:7], dob[8:10])
        sql = '''
            SELECT id FROM dangan WHERE DangAnHao=:archieve_id
        '''
        param = {'archieve_id': sh.cell(row, 3).value}
        res = db_engine.execute(text(' '.join(sql.split())), param)
        data = res.fetchall()
        if len(data) == 0:
            sql = '''
                INSERT INTO cm_archieve.dangan
                (DangAnHao, ShenFenZheng, XingMing, XingBie, ChuShengRiQi,
                    YuTuiXiuRiQi, RenYuanLeiBie, CunDangRiQi, CunDangZhuangTai)
                VALUES (:archieve_id, :identity, :name, :gender, :dob, :dor,
                    :cat, :arch_date, :arch_status)
            '''
            param = {'archieve_id': sh.cell(row, 3).value,
                'identity': sh.cell(row, 0).value,
                'name': sh.cell(row, 1).value,
                'gender': sh.cell(row, 2).value,
                'dob': dob,
                'dor': dor,
                'cat': sh.cell(row, 4).value,
                'arch_date': sh.cell(row, 5).value,
                'arch_status': sh.cell(row, 6).value}
            # param = (
            #     0, sh.cell(row, 3).value, sh.cell(row, 0).value,
            #     sh.cell(row, 1).value, sh.cell(row, 2).value, dob,
            #     dor, sh.cell(row, 4).value, sh.cell(row, 5).value,
            #     sh.cell(row, 6).value, 0, 0
            # )
        else:
            sql = '''
                update dangan
                set DangAnHao=:archieve_id, ShenFenZheng=:identity,
                    XingMing=:name, XingBie=:gender, ChuShengRiQi=:dob,
                    YuTuiXiuRiQi=:dor, RenYuanLeiBie=:cat,
                    CunDangRiQi=:arch_date, CunDangZhuangTai=:arch_status
                where id=:id
            '''
            param = {'archieve_id': sh.cell(row, 3).value,
                'identity': sh.cell(row, 0).value,
                'name': sh.cell(row, 1).value,
                'gender': sh.cell(row, 2).value,
                'dob': dob,
                'dor': dor,
                'cat': sh.cell(row, 4).value,
                'arch_date': sh.cell(row, 5).value,
                'arch_status': sh.cell(row, 6).value,
                'id': data[0].id}
        db_engine.execute(text(' '.join(sql.split())), param)


class DaoRu(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        return render_template('daoru.html', User=session['user_name'])

    def post(self):
        f = request.files['file']
        filename = secure_filename(f.filename)
        file_path = os.path.join(G_UPLOAD_PATH, filename)
        f.save(file_path)
        import_xls(file_path)
        return redirect('/daoru')


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
        return render_template('shangchuan.html',
            row=row, id=rec_id, filepath=fp, link=lp, cat=cat,
            User=session['user_name'])

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


class SaoMiao(MethodView):
    def get(self, uid):
        if not 'user_id' in session:
            return redirect('/login')
        url_root = request.url_root
        sql = '''
            SELECT * FROM dangan
            WHERE id=%s
        '''
        param = (
            uid,
        )
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if cursor.rowcount > 0:
            row = data[0]
        else:
            row = None
        close_db(cursor, cnx)
        fp = get_file_path(uid)
        return render_template('saomiao.html',
            filepath=fp,
            row=row,
            id=uid,
            url_root=url_root,
            User=session['user_name'])

#     def post(self, uid):
#         pass
#         p = get_file_path1(id)
#         with open('d:\\11231.jpg', 'wb') as f:
#             f.write(request.data)
#         f.close()
#         return 'Received'


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
            error=_err_message)

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
        sql = '''
            select id
            from dangan
            where danganhao=:aid
            or shenfenzheng=:id_card
        '''
        param = {'aid': _danganhao,
            'id_card': idcard_18}
        res = db_engine.execute(text(' '.join(sql.split())), param)
        data = res.fetchall()
        print(len(data))
        if len(data) > 0:
            return redirect('/luru?err=4')
        sql = '''
            INSERT INTO dangan
                (DangAnHao,ShenFenZheng,XingMing,XingBie,ChuShengRiQi,
                YuTuiXiuRiQi,NvGuanLiGangWei,TeShuGongZhong)
            VALUES
                (:archieve_id,:idcard,:name,:gender, :dob,
                :dor, :ngl, :stow)
        '''
        param = {'archieve_id': _danganhao,
            'idcard': idcard_18,
            'name': _name,
            'gender': gender,
            'dob': dob,
            'dor': dor,
            'ngl': s,
            'stow': t}
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rec_id = res.lastrowid
        res.close()
        caozuo_jilu(session['user_id'], u'添加档案信息', rec_id)
        return redirect('/saomiao/%s' % (rec_id))
