# -*- coding=UTF-8 -*-

import datetime
import sys
import time

from flask import render_template, session, redirect, request
from flask.views import MethodView

from globalvars import connect_db, close_db


class ChaXun(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')

        return render_template('chaxun.html', User = session['user_name'])

    def post(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        aid = request.form['DangAnHao']
        idcard = request.form['ShenFenZheng']
        name = request.form['XingMing']
        gender = request.form['XingBie']
        check = request.form.getlist('check')
        sql = '''
            select
                d.*,(
                    select
                        count(*)
                    from
                        cm_archieve.wenjian w
                    where
                        w.aid=d.id
                )
            from
                cm_archieve.dangan d
            where
                d.ZhuanChu=""
                or
                isNULL(d.ZhuanChu)
        '''
        if aid != '':
            sql = '%s AND DangAnHao LIKE "%s%s%s"' % (sql, '%', aid, '%')
        if idcard != '':
            sql = '%s AND ShenFenZheng LIKE "%s%s%s"' % (sql, '%', idcard, '%')
        if name != '':
            sql = '%s AND XingMing LIKE "%s%s%s"' % (sql, '%', name, '%')
        if gender == 'male':
            sql = '%s AND XingBie="%s"' % (sql, u'男')
        elif gender =='female':
            sql = '%s AND XingBie="%s"' % (sql, u'女')
        else:
            pass
        if 'ngl' in check:
            sql = '%s AND NvGuanLiGangWei=1' % (sql,)
        if 'stow' in check:
            sql = '%s AND TeShuGongZhong=1' % (sql,)
        sql = '%s LIMIT 100' % (sql,)
        #print(sql)
        cnx = onnect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        ose_db(cursor, cnx)
        return render_template('chaxun.html',
            data = data,
            User = session['user_name'])


class DangYueTuiXiu(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')

        t = time.localtime()
        time_str = time.strftime('%Y-%m', t)
        sql = 'SELECT * FROM dangan WHERE YuTuiXiuRiQi LIKE "' + \
            time_str + '%"'
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template(
            'dytx.html',
            data = data,
            User = session['user_name']
        )

    def post(self):
        if not 'user_id' in session:
            return redirect('/login')
        d = '%s-%s' % (request.form['year'], request.form['month'])
        sql = 'SELECT * FROM dangan WHERE YuTuiXiuRiQi LIKE "' + d + '%"'
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template(
            'dytx.html',
            data = result,
            user = session['user_name']
        )


class TeShuGongZhong(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        sql = 'SELECT * FROM dangan WHERE TeShuGongZhong=1'
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template(
            'tsgz.html',
            data = data,
            User = session['user_name']
        )


class NvGuanLiGangWei(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        sql = 'SELECT * FROM dangan WHERE NvGuanLiGangWei=1'
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template(
            'nglgw.html',
            data = data,
            User = session['user_name']
        )


#统计
#：各用户操作总数对比
#：按月份各用户操作总数曲线
#：按月份各用户扫描总数曲线
#：按月份各用户添加档案总数曲线

class TongJi(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        cnx = connect_db()
        cursor = cnx.cursor()
        sql_1 = '''
            select
                u.id,u.mingcheng,count(c.id)
            from
                `cm_archieve`.user u
                left join
                `cm_archieve`.caozuo_jilu c
                on
                u.id=c.yh_id
            group by
                u.id
        '''
        cursor.execute(sql_1)
        result_1 = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template(
            'tongji.html',
            User = session['user_name'],
            counter_1 = result_1,
        )


class TongjiMonth(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        _year = request.args.get('year', datetime.datetime.now().strftime('%Y'))
        _month = request.args.get('month', 
            datetime.datetime.now().strftime('%m'))
        _date = '%s-%s' % (_year, _month)
        sql = ('select u.MingCheng,('
            'select count(*) as yh_count '
            'from ('
            'select yh_id,count(*) '
            'from cm_archieve.caozuo_jilu c '
            'where c.caozuo="上传图片" '
            'and locate(%(date)s,c.riqi) > 0 '
            'group by yh_id,neirong '
            ') as yh '
            'where yh.yh_id=u.id '
            ') as yh_count '
            'from cm_archieve.user as u')
        param = {
            'date': _date
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        res = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template('tongji_month.html',
            counter_1=res,
            date=_date)

    def post(self):
        year = request.form['year']
        month = request.form['month']

        return redirect('/tongji_month/?year=%s&month=%s' % (year, month))

