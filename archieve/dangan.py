# -*- coding=UTF-8 -*-

import os
import datetime
import zipfile

import globalvars

from random import randint

from flask import session, redirect, request, render_template
from flask.views import MethodView
from sqlalchemy import text

from globalvars import *


class DangAn(MethodView):
    def get(self, rec_id):
        if not 'user_id' in session:
            return redirect('/login')
        cat = request.args.get('cat', '0')
        sql = '''
            select d.*,(
                select a.code
                from cm_archieve.access_code a
                where a.date=:now_date
                and a.archieve_id=d.ShenFenZheng
                order by a.id desc
                limit 1
            ) as code
            from cm_archieve.dangan d
            where d.id=:archieve_id
        '''
        param = {
            'archieve_id': rec_id,
            'now_date': datetime.datetime.now().strftime('%Y-%m-%d')
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        row = res.fetchone()
        res.close()
        dob = row[5].split('-')
        dor = row[6].split('-')
        if cat == '0':
            sql = 'SELECT * FROM wenjian WHERE aid=:archieve_id'
            param = {'archieve_id': rec_id}
        else:
            sql = '''
                SELECT *
                FROM wenjian
                WHERE aid=:archieve_id
                AND LeiBie=%:cat
            '''
            param = {'archieve_id': rec_id,
                'cat': cat}
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows_pic = res.fetchall()
        res.close()
        sql = '''
            select auth_del_archieve
            from user
            where id=:id
        '''
        param = {'id': session['user_id']}
        print(session['user_id'])
        res = db_engine.execute(text(' '.join(sql.split())), param)
        row_auth = res.fetchone()
        res.close()
        print(row_auth)
        lp1 = '/saomiao/%s' % (rec_id,)
        lp2 = '/luru/%s' % (rec_id,)
        return render_template('dangan.html',
            id=rec_id, row=row, link1=lp1, link2=lp2,
            fs_root=G_FILE_SERVER_ROOT, aid=get_aid(rec_id),
            data1=rows_pic, dob=dob, dor=dor, cat=cat, auth=row_auth,
            User=session['user_name'])


    def post(self, rec_id):
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
        param = (dob, dor, s, t, name, idcard, gender, rec_id)
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        cnx.commit()
        close_db(cursor, cnx)
        caozuo_jilu(session['user_id'], u'修改档案信息', rec_id)
        return redirect('/dangan/%s' % (rec_id))


class DeleteArchieve(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        archieve_id = request.args.get('archieve_id')
        sql = '''
            delete from dangan
            where id=:id
        '''
        param = {'id': archieve_id}
        db_engine.execute(text(' '.join(sql.split())), param)
        caozuo_jilu(session['user_id'], u'删除档案', archieve_id)
        return redirect('/')


class MakeVoid(MethodView):
    def post(self, archieve_id):
        sql = '''
            update dangan
            set ZhuanChu=:zhuanchu
            where id=:archieve_id
        '''
        param = {'zhuanchu': request.form['reason'],
            'archieve_id': archieve_id}
        db_engine.execute(text(' '.join(sql.split())), param)
        return redirect('/')


class DownloadZip(MethodView):
    def get(self, archieve_id):
        sql = '''
            select danganhao
            from dangan
            where id=%(archieve_id)s
        '''
        param = {'archieve_id': archieve_id}
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        archieve_path = os.path.join(G_UPLOAD_PATH, result[0][0])
        sql = '''
            select wenjianming
            from wenjian
            where aid=%(archieve_id)s
            and client_access=1
        '''
        param = {'archieve_id': archieve_id}
        cursor.execute(sql, param)
        file_list = cursor.fetchall()
        zip_file = zipfile.ZipFile(os.path.join(archieve_path, 'file.zip'),
            'w', zipfile.ZIP_DEFLATED)
        for f in file_list:
            zip_file.write(os.path.join(archieve_path, f[0]), f[0])
        zip_file.close()
        close_db(cursor, cnx)
        p = os.path.join(archieve_path, 'file.zip')
        return render_template('dl_zip.html',
            archieve_id=archieve_id,
            archieve=result[0][0])


class DaYin(MethodView):
    def get(self, archieve_id):
        pic_id = request.args.get('pic_id')
        if pic_id == '':
            redirect('/')
        sql = '''
            select d.DangAnHao,(
                select w.WenJianMing
                from cm_archieve.wenjian w
                where w.id=%(pic_id)s
                and w.aid=d.id
            ) as pic_name
            from cm_archieve.dangan d
            where d.id=%(archieve_id)s
        '''
        param = {
            'pic_id': pic_id,
            'archieve_id': archieve_id
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        close_db(cursor, cnx)
        file_name = '%s\%s\%s' % (G_UPLOAD_PATH, result[0][0], result[0][1])
        render_text(file_name=file_name,
            font_size=32,
            text=u'与原件相符',
            output_name='%s/%s/for_print.png' % (G_UPLOAD_PATH, result[0][0]),
            output_type='png')
        caozuo_jilu(session['user_id'], u'打印', archieve_id)
        return '<img src="/static/upload/%s/for_print.png" />' % \
            (result[0][0])


class ChaKan(MethodView):
    def get(self, rec_id):
        if not 'user_id' in session:
            return redirect('/login')
        pic_id = request.args.get('pic_id', '0')
        sql = '''
            SELECT w.id,w.aid,w.wenjianming,d.danganhao,w.client_access
            FROM wenjian as w
            INNER JOIN dangan as d
            ON w.aid=d.id
            WHERE w.id=%(pic_id)s
        '''
        param = {'pic_id': pic_id}
        sql_t = '''
            select id
            from `cm_archieve`.wenjian
            where id = (
                select max(id)
                from wenjian
                where id<%(rec_id)s
                and aid=%(archieve_id)s
            ) or id = (
                select min(id)
                from wenjian
                where id>%(rec_id)s
                and aid=%(archieve_id)s
            )
        '''
        param_t = {
            'archieve_id': rec_id,
            'rec_id': pic_id
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        cursor.execute(sql_t, param_t)
        result = cursor.fetchall()
        if cursor.rowcount == 0:
            previous_id = None
            next_id = None
        else:
            if int(result[0][0]) < int(pic_id):
                previous_id = result[0][0]
                if len(result) == 2:
                    previous_id = result[0][0]
                    next_id = result[1][0]
                else:
                    next_id = None
            else:
                previous_id = None
                next_id = result[0][0]
        close_db(cursor, cnx)
        row = data[0]
        return render_template('chakan.html',
            fs_root=G_FILE_SERVER_ROOT,
            aid=row[3],
            row=row,
            User=session['user_name'],
            archieve_id=rec_id,
            previous_id=previous_id,
            next_id=next_id,
            pic_id=pic_id)


    def post(self, rec_id):
        opr = request.form['operate']
        pic_id = request.args.get('pic_id', '')
        if opr == 'turn':
            sql = '''
                SELECT w.id,w.aid,w.wenjianming,d.danganhao
                FROM wenjian w INNER JOIN dangan d ON w.aid=d.id
                WHERE w.id=%s
            '''
            param = (pic_id,)
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            row = data[0]
            turn_image(
                '%s\%s\%s' % \
                (G_UPLOAD_PATH, row[3], row[2])
            )
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'rotate':
            sql = '''
                SELECT w.id,w.aid,w.wenjianming,d.danganhao
                FROM wenjian w INNER JOIN dangan d ON w.aid=d.id
                WHERE w.id=%s
            '''
            param = (pic_id,)
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            row = data[0]
            rotate_image('%s\%s\%s' % \
                (G_UPLOAD_PATH, row[3], row[2]))
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'delete':
            sql = '''
                SELECT w.id,w.aid,w.wenjianming,d.danganhao
                FROM wenjian w INNER JOIN dangan d ON w.aid=d.id
                WHERE w.id=%s
            '''
            param = (pic_id,)
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            sql = 'DELETE FROM wenjian WHERE id=%s'
            param = (pic_id,)
            cursor.execute(sql, param)
            cnx.commit()
            row = data[0]
            fp = '%s\%s\%s' % (G_UPLOAD_PATH, row[3], row[2])
            if os.path.isfile(fp):
                os.remove(fp)
            close_db(cursor, cnx)
            return redirect('/dangan/%s' % rec_id)
        elif opr == 'access':
            sql = '''
                UPDATE wenjian
                SET client_access=%(client_access)s
                WHERE id=%(pic_id)s
            '''
            param = {
                'client_access': 1,
                'pic_id': pic_id,
            }
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'cancel_access':
            sql = '''
                UPDATE wenjian
                SET client_access=%(client_access)s
                WHERE id=%(pic_id)s
            '''
            param = {
                'client_access': 0,
                'pic_id': pic_id,
            }
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat1':
            sql = ('update '
                'wenjian '
                'set '
                'leibie=1 '
                'where '
                'id=%(pic_id)s')
            param = {'pic_id': pic_id}
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat2':
            sql = ('update wenjian set leibie=2 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat3':
            sql = ('update wenjian set leibie=3 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat4':
            sql = ('update wenjian set leibie=4 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat5':
            sql = ('update wenjian set leibie=5 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat6':
            sql = ('update wenjian set leibie=6 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat7':
            sql = ('update wenjian set leibie=7 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat8':
            sql = ('update wenjian set leibie=8 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat9':
            sql = ('update wenjian set leibie=9 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        else:
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))

class UploadImageFile(MethodView):
    def post(self):
        rec_id = request.args.get('id', '')
        cat = request.args.get('cat', '1')
        aid = get_aid(rec_id)
        fp = '%s\\%s' % (_UPLOAD_PATH, aid)
        check_path(fp)
        file_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        file_name = '%s.jpg' % (file_time)
        fp = '%s\\%s' % (fp, file_name)
        with open(fp, 'wb') as f:
            f.write(request.data)
        f.close()
        sql = '''
            INSERT INTO wenjian
            (aid, LeiBie, WenJianMing)
            VALUES(%s, %s, %s)
        '''
        param = (rec_id, cat, file_name)
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        cnx.commit()
        lose_db(cursor, cnx)
        rotate_image(fp)
        caozuo_jilu(session['user_id'], u'上传图片', rec_id)
        return u'完成'


class GenCode(MethodView):
    def get(self, archieve_id):
        code = randint(1000, 9999)
        date = datetime.datetime.now()
        sql = '''
            SELECT shenfenzheng FROM dangan
            WHERE id=%(archieve_id)s
        '''
        param = {'archieve_id': archieve_id, }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        sql = '''
            INSERT INTO access_code (
                archieve_id, code, date
            )
            VALUES(
                %(archieve_id)s, %(code)s, %(date)s
            )
        '''
        param = {
            'archieve_id': result[0][0],
            'code': code,
            'date': date.strftime('%Y-%m-%d'),
        }
        cursor.execute(sql, param)
        cnx.commit()
        close_db(cursor, cnx)
        caozuo_jilu(session['user_id'], u'生成查询密码', archieve_id)
        return redirect('/dangan/%s' % archieve_id)


class Exp2Client(MethodView):
    def post(self, rec_id):
        pic_id = request.form.getlist('pic_id')
        sql = ('select * '
            'from wenjian '
            'where aid=%(archieve_id)s')
        param = {'archieve_id': rec_id}
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        for row in result:
            if str(row[0]) in pic_id:
                sql = ('UPDATE wenjian '
                    'SET client_access=%(client_access)s '
                    'WHERE id=%(pic_id)s')
                param = {
                    'client_access': 1,
                    'pic_id': row[0],
                }
                cursor.execute(sql, param)
            else:
                sql = ('UPDATE wenjian '
                    'SET client_access=%(client_access)s '
                    'WHERE id=%(pic_id)s')
                param = {
                    'client_access': 0,
                    'pic_id': row[0],
                }
                cursor.execute(sql, param)
        cnx.commit()
        close_db(cursor, cnx)
        caozuo_jilu(session['user_id'], u'导出到终端', rec_id)
        return redirect('/dangan/%s' % (rec_id,))
