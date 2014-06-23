# -*- coding=UTF-8 -*-

import sys

from flask import redirect, render_template, session, request
from flask.views import MethodView
from sqlalchemy import text

from globalvars import *


reload(sys)
sys.setdefaultencoding('utf-8')


class Home(MethodView):
    def get(self):
        if not session['user_account'] in G_VIEW_USER:
            return redirect('/logout')
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
        return render_template('view_home.html', user_name=session['user_name'],
            count_1=row_user.count, count_2=row_archieve.count,
            count_3=row_archieve_scaned.count)


class User(MethodView):
    def get(self):
        if not session['user_account'] in G_VIEW_USER:
            return redirect('/logout')
        sql = '''
            select *
            from user
        '''
        res = db_engine.execute(text(' '.join(sql.split())))
        rows = res.fetchall()
        res.close()
        return render_template('view_user.html',
            user_name=session['user_name'],
            rows=rows)


class Archieve(MethodView):
    def get(self):
        if not session['user_account'] in G_VIEW_USER:
            return redirect('/logout')
        archieve_id = request.args.get('archieve_id')
        id_card = request.args.get('id_card')
        name = request.args.get('name')
        gender = request.args.get('gender')
        ngl = request.args.get('ngl')
        stow = request.args.get('stow')
        sql = '''
            select d.*,(
                select count(*)
                from cm_archieve.wenjian w
                where w.aid=d.id
            ) as page_count
            from cm_archieve.dangan d
            where (d.ZhuanChu=""
            or d.ZhuanChu is null)
        '''
        if archieve_id:
            sql += '\nand locate(:archieve_id,DangAnHao)>0'
        if id_card:
            sql += '\nand locate(:id_card,ShenFenZheng)>0'
        if name:
            sql += '\nand locate(:name,XingMing)>0'
        if gender:
            sql += '\nand d.XingBie=:gender'
        if ngl == '1':
            sql += '\nand d.NvGuanLiGangWei=1'
        else:
            sql += '\nand d.NvGuanLiGangWei=0'
        if stow == '1':
            sql += '\nand d.TeShuGongZhong=1'
        else:
            sql += '\nand d.TeShuGongZhong=0'
        sql += '\nlimit 20'
        param = {
            'archieve_id': archieve_id,
            'id_card': id_card,
            'name': name,
            'gender': gender,
        }
        print(sql)
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('view_archieve.html',
            user_name=session['user_name'], rows=rows)

    def post(self):
        archieve_id = request.form['DangAnHao']
        id_card = request.form['ShenFenZheng']
        name = request.form['XingMing']
        gender = request.form['XingBie']
        check = request.form.getlist('check')
        check_1 = check_2 = 0
        if 'ngl' in check:
            check_1 = 1
        if 'stow' in check:
            check_2 = 1
        p = 'archieve_id=%s&id_card=%s&name=%s&gender=%s&ngl=%s&stow=%s' % \
            (archieve_id, id_card, name, gender, check_1, check_2)
        return redirect('/view/archieve?%s' % (p))
#         sql = '''
#             select d.*,(
#                 select count(*)
#                 from cm_archieve.wenjian w
#                 where w.aid=d.id
#             ) as page_count
#             from cm_archieve.dangan d
#             where d.ZhuanChu=""
#             or d.ZhuanChu is null
#         '''
#         if aid != '':
#             sql = '%s and d.DangAnHao like "%s%s%s"' % (sql, '%', archieve_id, '%')
#         if idcard != '':
#             sql = '%s AND d.ShenFenZheng LIKE "%s%s%s"' % (sql, '%', idcard, '%')
#         if name != '':
#             sql = '%s AND d.XingMing LIKE "%s%s%s"' % (sql, '%', name, '%')
#         if gender == 'male':
#             sql = '%s AND d.XingBie="%s"' % (sql, u'男')
#         elif gender == 'female':
#             sql = '%s AND d.XingBie="%s"' % (sql, u'女')
#         else:
#             pass
#         if 'ngl' in check:
#             sql = '%s AND d.NvGuanLiGangWei=1' % (sql,)
#         if 'stow' in check:
#             sql = '%s AND d.TeShuGongZhong=1' % (sql,)
#         sql = '%s LIMIT 20' % (sql)
        # print(sql)
#         sql = '''
#             select d.*,(
#                 select count(*)
#                 from cm_archieve.wenjian w
#                 where w.aid=d.id
#             ) as page_count
#             from cm_archieve.dangan d
#             where d.ZhuanChu=""
#             or d.ZhuanChu is null
#         '''
#         if archieve_id:
#             sql += 'and locate(:archieve_id,d.DangAnHao)>0'
#         if id_card:
#             sql += 'and locate(:id_card,d.ShenFenZheng)>0'
#         if name:
#             sql += 'and locate(:name,d.XingMing)>0'
#         if gender:
#             sql += 'and d.XingBie=:gender'
#         if 'ngl' in check:
#             sql += 'and d.NvGuanLiGangWei=1'
#         if 'stow' in check:
#             sql += 'and d.TeShuGongZhong=1'
#         sql += 'limit 20'
#         print(sql)
#         res = db_engine.execute(text(' '.join(sql.split())), param)
#         rows = res.fetchall()


class Statistics(MethodView):
    def get(self):
        if not session['user_account'] in G_VIEW_USER:
            return redirect('/logout')
