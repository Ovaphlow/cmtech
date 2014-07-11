# -*- coding=UTF-8 -*-

import datetime
import sys
import time

from flask import render_template, session, redirect, request
from flask.views import MethodView
from sqlalchemy import text

from globalvars import *


class ChaXun(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        return render_template('chaxun.html', User=session['user_name'])

    def post(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        aid = request.form['DangAnHao']
        idcard = request.form['ShenFenZheng']
        name = request.form['XingMing']
        gender = request.form['XingBie']
        check = request.form.getlist('check')
        sql = '''
            select d.*,(
                select count(*)
                from cm_archieve.wenjian w
                where w.aid=d.id
            ) as page_count
            from cm_archieve.dangan d
            where d.ZhuanChu=""
            or isNULL(d.ZhuanChu)
        '''
        if aid != '':
            sql = '%s AND d.DangAnHao LIKE "%s%s%s"' % (sql, '%', aid, '%')
        if idcard != '':
            sql = '%s AND d.ShenFenZheng LIKE "%s%s%s"' % (sql, '%', idcard, '%')
        if name != '':
            sql = '%s AND d.XingMing LIKE "%s%s%s"' % (sql, '%', name, '%')
        if gender == 'male':
            sql = '%s AND d.XingBie="%s"' % (sql, u'男')
        elif gender == 'female':
            sql = '%s AND d.XingBie="%s"' % (sql, u'女')
        else:
            pass
        if 'ngl' in check:
            sql = '%s AND d.NvGuanLiGangWei=1' % (sql,)
        if 'stow' in check:
            sql = '%s AND d.TeShuGongZhong=1' % (sql,)
        sql = '%s LIMIT 100' % (sql,)
        # print(sql)
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template('chaxun.html',
            data=data,
            User=session['user_name'])


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
        return render_template('dytx.html',
            data=data,
            User=session['user_name'])

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
        return render_template('dytx.html',
            data=result,
            user=session['user_name'])


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
        return render_template('tsgz.html',
            data=data,
            User=session['user_name'])


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
        return render_template('nglgw.html',
            data=data,
            User=session['user_name'])


# 统计
# ：各用户操作总数对比
# ：按月份各用户操作总数曲线
# ：按月份各用户扫描总数曲线
# ：按月份各用户添加档案总数曲线

# 2014-07-04
# 一、档案扫描录入统计
# 1.档案扫描总量统计
# 2.分月份统计，统计结果单击操作员可出现该操作员已扫描档案列表
# 3.分时间段统计，选择起始日期和终止日期，统计该事件段内所有操作员扫描情况，单击操作员可出现
#   已扫描档案列表
# 4.按档案号码输入可查询到该档案由哪个操作员什么时间扫描
# 二、档案利用操作统计
# 按月及时间段统计档案材料打印、自助查询密码设置数量（册、页），及单击可列表具体的档案号码。
# 输入档案号码可查该档案材料是否被利用过，利用时间，操作员。

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
            where c.caozuo="上传图片"
            group by
                u.id
        '''
        cursor.execute(sql_1)
        result_1 = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template('tongji.html',
            User=session['user_name'],
            counter_1=result_1)


class TongjiMonth(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        _year = datetime.datetime.now().strftime('%Y')
        _month = datetime.datetime.now().strftime('%m')
        _date = '%s-%s' % (_year, _month)
        sql = '''
            select u.MingCheng,(
                select count(*) as yh_count
                from (
                    select yh_id,count(*)
                    from cm_archieve.caozuo_jilu c
                    where c.caozuo="上传图片"
                    and locate(%(date)s,c.riqi) > 0
                    group by yh_id,neirong
                ) as yh
                where yh.yh_id=u.id
            ) as yh_count
            from cm_archieve.user as u
        '''
        param = {'date': _date}
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        res = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template('tongji_month.html',
            User=session['user_name'],
            counter_1=res,
            date=_date)


class TongjiTimeSlot(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('login')
        if request.args.get('year_begin'):
            year_begin = request.args.get('year_begin')
        else:
            year_begin = datetime.datetime.now().strftime('%Y')
        if request.args.get('month_begin'):
            month_begin = request.args.get('month_begin')
        else:
            month_begin = datetime.datetime.now().strftime('%m')
        if request.args.get('day_begin'):
            day_begin = request.args.get('day_begin')
        else:
            day_begin = '01'
        if request.args.get('year_end'):
            year_end = request.args.get('year_end')
        else:
            year_end = year_begin
        if request.args.get('month_end'):
            month_end = request.args.get('month_end')
        else:
            month_end = month_begin
        if request.args.get('day_end'):
            day_end = request.args.get('day_end')
        else:
            day_end = '31'
        # print(year_begin, month_begin, day_begin)
        # print(year_end, month_end, day_end)
        date_begin = '%s-%s-%s' % (year_begin, month_begin, day_begin)
        date_end = '%s-%s-%s' % (year_end, month_end, day_end)
        sql = '''
            select u.id,u.mingcheng,count(c.id) as counter
            from `cm_archieve`.user u
            left join `cm_archieve`.caozuo_jilu c
            on u.id=c.yh_id
            where c.caozuo="上传图片"
            and c.riqi>:date_begin
            and c.riqi<:date_end
            group by u.id
        '''
        param = {
            'date_begin': date_begin,
            'date_end': date_end
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('tongji_time_slot.html',
            User=session['user_name'], rows=rows,
            date_begin=date_begin, date_end=date_end)

    def post(self):
        uri = '/tongji_time_slot?'
        uri += 'year_begin=%s' % (request.form['year_begin'])
        uri += '&month_begin=%s' % (request.form['month_begin'])
        uri += '&day_begin=%s' % (request.form['day_begin'])
        uri += '&year_end=%s' % (request.form['year_end'])
        uri += '&month_end=%s' % (request.form['month_end'])
        uri += '&day_end=%s' % (request.form['day_end'])
        return redirect(uri)


class ArchieveLog(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('login')
        archieve_id = request.args.get('archieve_id', 0)
        sql = '''
            select d.id,d.danganhao, c.yh_id,c.riqi,u.mingcheng
            from dangan as d
            left join caozuo_jilu as c
            on c.NeiRong=d.id
            left join user as u
            on c.yh_id=u.id
            where c.CaoZuo=:operation
            and d.danganhao=:archieve_id
        '''
        param = {
            'operation': u'上传图片',
            'archieve_id': archieve_id
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('statistics/archieve_log.html',
            User=session['user_name'], rows=rows)

    def post(self):
        archieve_id = request.form['archieve_id']
        return redirect('/tongji_archieve_log?archieve_id=%s' % (archieve_id))


class PrintTimeSlot(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('login')
        
