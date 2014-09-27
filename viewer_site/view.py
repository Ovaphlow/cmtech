# -*- coding=UTF-8 -*-

import sys
import datetime

from flask import redirect, render_template, session, request
from flask.views import MethodView
from sqlalchemy import text

from globalvars import *


reload(sys)
sys.setdefaultencoding('utf-8')


class Home(MethodView):
    def get(self):
        sql = '''
            select count(*) as count
            from user
        '''
        res = db_engine.execute(text(' '.join(sql.split())))
        row_user = res.fetchone()
        res.close()
        sql = '''
            select count(*) as count
            from dangan
        '''
        res = db_engine.execute(text(' '.join(sql.split())))
        row_archieve = res.fetchone()
        res.close()
        sql = '''
            select count(*) as count
            from (
                select d.id
                from dangan d
                inner join wenjian w
                on d.id=w.aid
                group by d.id
            ) as a
        '''
        res = db_engine.execute(text(' '.join(sql.split())))
        row_archieve_scaned = res.fetchone()
        res.close()
        return render_template('viewer_site/home.html',
            count_1=row_user.count, count_2=row_archieve.count,
            count_3=row_archieve_scaned.count)


class InputArchieveId(MethodView):
    def get(self):
        err = None
        return render_template('viewer_site/input_archieve_id.html',
            error_message=err)

    def post(self):
        archieve_id = request.form['archieve_id']
        return redirect('/view/archieve_list?archieve_id=%s' % \
            (archieve_id))


class InputIdentityCard(MethodView):
    def get(self):
        err = None
        return render_template('viewer_site/input_identity_card.html',
            error_message=err)

    def post(self):
        identity_card = request.form['identity_card']
        return redirect('/view/archieve_list?identity_card=%s' % \
            (identity_card))


class ArchieveList(MethodView):
    def get(self):
        archieve_id = request.args.get('archieve_id', None)
        identity_card = request.args.get('identity_card', None)
        if archieve_id:
            sql = '''
                select d.*,(
                    select count(*)
                    from cm_archieve.wenjian w
                    where w.aid=d.id
                ) as page_count
                from cm_archieve.dangan d
                where (d.ZhuanChu=""
                or d.ZhuanChu is null)
                and locate(:archieve_id,danganhao)>0
            '''
            param = {'archieve_id': archieve_id}
        if identity_card:
            sql = '''
                select d.*,(
                    select count(*)
                    from cm_archieve.wenjian w
                    where w.aid=d.id
                ) as page_count
                from cm_archieve.dangan d
                where (d.ZhuanChu=""
                or d.ZhuanChu is null)
                and locate(:identity_card,shenfenzheng)>0
            '''
            param = {'identity_card': identity_card}
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('viewer_site/archieve_list.html',
            rows=rows)


# class User(MethodView):
#     def get(self):
#         sql = '''
#             select *
#             from user
#         '''
#         res = db_engine.execute(text(' '.join(sql.split())))
#         rows = res.fetchall()
#         res.close()
#         return render_template('viewer_site/user.html',
#             rows=rows)


# class Archieve(MethodView):
#     def get(self):
#         archieve_id = request.args.get('archieve_id')
#         id_card = request.args.get('id_card')
#         name = request.args.get('name')
#         gender = request.args.get('gender')
#         ngl = request.args.get('ngl')
#         stow = request.args.get('stow')
#         sql = '''
#             select d.*,(
#                 select count(*)
#                 from cm_archieve.wenjian w
#                 where w.aid=d.id
#             ) as page_count
#             from cm_archieve.dangan d
#             where (d.ZhuanChu=""
#             or d.ZhuanChu is null)
#         '''
#         if archieve_id:
#             sql += '\nand locate(:archieve_id,DangAnHao)>0'
#         if id_card:
#             sql += '\nand locate(:id_card,ShenFenZheng)>0'
#         if name:
#             sql += '\nand locate(:name,XingMing)>0'
#         if gender:
#             sql += '\nand d.XingBie=:gender'
#         if ngl == '1':
#             sql += '\nand d.NvGuanLiGangWei=1'
#         else:
#             sql += '\nand d.NvGuanLiGangWei=0'
#         if stow == '1':
#             sql += '\nand d.TeShuGongZhong=1'
#         else:
#             sql += '\nand d.TeShuGongZhong=0'
#         sql += '\nlimit 20'
#         param = {
#             'archieve_id': archieve_id,
#             'id_card': id_card,
#             'name': name,
#             'gender': gender,
#         }
#         res = db_engine.execute(text(' '.join(sql.split())), param)
#         rows = res.fetchall()
#         res.close()
#         return render_template('viewer_site/archieve.html',
#             rows=rows)
#
#     def post(self):
#         archieve_id = request.form['DangAnHao']
#         id_card = request.form['ShenFenZheng']
#         name = request.form['XingMing']
#         gender = request.form['XingBie']
#         check = request.form.getlist('check')
#         check_1 = check_2 = 0
#         if 'ngl' in check:
#             check_1 = 1
#         if 'stow' in check:
#             check_2 = 1
#         p = 'archieve_id=%s&id_card=%s&name=%s&gender=%s&ngl=%s&stow=%s' % \
#             (archieve_id, id_card, name, gender, check_1, check_2)
#         return redirect('/view/archieve?%s' % (p))


class ArchieveDetail(MethodView):
    def get(self):
        archieve_id = request.args.get('archieve_id')
        sql = '''
            select *
            from dangan
            where id=:archieve_id
        '''
        param = {'archieve_id': archieve_id}
        res = db_engine.execute(text(' '.join(sql.split())), param)
        row = res.fetchone()
        res.close()
        sql = '''
            select *
            from wenjian
            where aid=:archieve_id
        '''
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('viewer_site/archieve_detail.html',
            row=row, rows=rows,
            file_uri=ARCHIEVE_FILE_URI)


# class Statistics(MethodView):
#     def get(self):
#         sql = '''
#             select u.id,u.mingcheng,count(c.id) as counter
#             from `cm_archieve`.user u
#             left join `cm_archieve`.caozuo_jilu c
#             on u.id=c.yh_id
#             group by u.id
#         '''
#         res = db_engine.execute(text(' '.join(sql.split())))
#         rows_1 = res.fetchall()
#         res.close()
#         sql = '''
#             select u.MingCheng,(
#                 select count(*) as yh_count
#                 from (
#                     select yh_id,count(*)
#                     from cm_archieve.caozuo_jilu c
#                     where c.caozuo="上传图片"
#                     and locate(:month,c.riqi) > 0
#                     group by yh_id,neirong
#                 ) as yh
#                 where yh.yh_id=u.id
#             ) as yh_count
#             from cm_archieve.user as u
#         '''
#         param = {'month': datetime.datetime.now().strftime('%Y-%m')}
#         res = db_engine.execute(text(' '.join(sql.split())), param)
#         rows_month = res.fetchall()
#         res.close()
#         return render_template('viewer_site/statistics.html',
#             rows_1=rows_1, rows_month=rows_month)
