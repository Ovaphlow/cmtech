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
        return render_template('statistics/chaxun.html', User=session['user_name'])

    def post(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        aid = request.form['DangAnHao']
        idcard = request.form['ShenFenZheng']
        name = request.form['XingMing']
        check = request.form.getlist('check')
        sql = '''
            select d.*,(
                select id
                from wenjian w
                where w.aid=d.id
                limit 1
            ) as scanned
            from dangan d
            where (d.ZhuanChu=""
            or d.ZhuanChu is null)
        '''
        if aid:
            sql += '''
                and locate(:archieve_id,d.danganhao)>0
            '''
        if idcard:
            sql += '''
                and locate(:id_card,d.shenfenzheng)>0
            '''
        if name:
            sql += '''
                and locate(:name,d.XingMing)>0
            '''
        if 'ngl' in check:
            sql += '''
                and d.nvguanligangwei=1
            '''
        if 'stow' in check:
            sql += '''
                and d.teshugongzhong=1
            '''
        sql += '''
            order by d.danganhao
            limit 100
        '''
        param = {
            'archieve_id': aid,
            'id_card': idcard,
            'name': name,
        }
        # print(sql)
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('statistics/chaxun.html',
            User=session['user_name'], archieve=rows)


class ScanLog(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        user_id = request.args.get('user_id', 0)
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        date_begin = request.args.get('date_begin', today)
        date_end = request.args.get('date_end', today)
        sql = '''
            select *
            from user
        '''
        res = db_engine.execute(text(' '.join(sql.split())))
        rows_user = res.fetchall()
        res.close()
        sql = '''
            select d.id,d.DangAnHao,d.ShenFenZheng,d.XingMing,d.XingBie,
                d.ChuShengRiQi,d.YuTuiXiuRiQi
            from dangan as d
            left join caozuo_jilu as c
            on d.id=c.neirong
            where (d.ZhuanChu=""
                or d.ZhuanChu is null)
            and c.caozuo=:operation
            and c.yh_id=:user_id
            and c.riqi>=:date_begin
            and c.riqi<=:date_end
            group by c.neirong
        '''
        param = {
            'operation': u'上传图片',
            'user_id': user_id,
            'date_begin': date_begin,
            'date_end': date_end
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('statistics/scan_log.html',
            User=session['user_name'], users=rows_user, rows=rows,
            user_id_sel=int(user_id), date_begin=date_begin, date_end=date_end)

    def post(self):
        user_id = request.form['user_id']
        year_begin = request.form['year_begin']
        month_begin = request.form['month_begin']
        day_begin = request.form['day_begin']
        year_end = request.form['year_end']
        month_end = request.form['month_end']
        day_end = request.form['day_end']
        uri = '/chaxun/scan_log?'
        uri += 'user_id=%s' % (user_id)
        uri += '&date_begin=%s-%s-%s' % (year_begin, month_begin, day_begin)
        uri += '&date_end=%s-%s-%s' % (year_end, month_end, day_end)
        return redirect(uri)


class InvokeLogUser(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        user_id = request.args.get('user_id', 0)
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        date_begin = request.args.get('date_begin', today)
        date_end = request.args.get('date_end', today)
        sql = '''
            select id,MingCheng
            from user
        '''
        res = db_engine.execute(text(' '.join(sql.split())))
        rows_user = res.fetchall()
        res.close()
        sql = '''
            select d.id,d.DangAnHao,d.ShenFenZheng,d.XingMing,d.XingBie,
                c.CaoZuo,c.RiQi
            from caozuo_jilu as c
            left join dangan as d
            on c.NeiRong=d.id
            where (d.ZhuanChu=""
                or d.ZhuanChu is null)
            and (c.caozuo=:operation_1
                or c.caozuo=:operation_2
                or c.caozuo=:operation_3)
            and c.yh_id=:user_id
            and c.riqi>=:date_begin
            and c.riqi<=:date_end
        '''
        param = {
            'operation_1': u'打印',
            'operation_2': u'生成查询密码',
            'operation_3': u'导出到终端',
            'user_id': user_id,
            'date_begin': date_begin,
            'date_end': date_end
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('statistics/invoke_log_user.html',
            User=session['user_name'], users=rows_user, rows=rows,
            user_id_sel=int(user_id), date_begin=date_begin, date_end=date_end)

    def post(self):
        user_id = request.form['user_id']
        year_begin = request.form['year_begin']
        month_begin = request.form['month_begin']
        day_begin = request.form['day_begin']
        year_end = request.form['year_end']
        month_end = request.form['month_end']
        day_end = request.form['day_end']
        uri = '/chaxun/invoke_log_user?'
        uri += 'user_id=%s' % (user_id)
        uri += '&date_begin=%s-%s-%s' % (year_begin, month_begin, day_begin)
        uri += '&date_end=%s-%s-%s' % (year_end, month_end, day_end)
        return redirect(uri)


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
        return render_template('statistics/dytx.html',
            data=data, User=session['user_name'])

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
        return render_template('statistics/dytx.html',
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
        return render_template('statistics/tsgz.html',
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
        return render_template('statistics/nglgw.html',
            data=data,
            User=session['user_name'])


class TongJi(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        sql = '''
            select u.MingCheng,u.id,(
              	select count(*) as yh_count
              	from (
                		select yh_id,count(*)
                		from caozuo_jilu c
                		where c.caozuo=:operation
                		group by yh_id,neirong
              	) as yh
              	where yh.yh_id=u.id
            ) as counter
            from user as u
        '''
        param = {'operation': u'上传图片'}
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('statistics/tongji.html',
            User=session['user_name'], counter_1=rows)


class TongjiMonth(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        _date = datetime.datetime.now().strftime('%Y-%m')
        sql = '''
            select u.MingCheng,u.id,(
                select count(*) as yh_count
                from (
                    select yh_id,count(*)
                    from cm_archieve.caozuo_jilu c
                    where c.caozuo=:operation
                    and locate(:date,c.riqi)>0
                    group by yh_id,neirong
                ) as yh
                where yh.yh_id=u.id
            ) as yh_count
            from cm_archieve.user as u
        '''
        param = {
            'date': _date,
            'operation': u'上传图片'
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('statistics/tongji_month.html',
            User=session['user_name'], counter_1=rows, date=_date)


class TongjiTimeSlot(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('login')
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        date_begin = request.args.get('date_begin', today)
        date_end = request.args.get('date_end', today)
        sql = '''
            select u.MingCheng,u.id,(
                select count(*) as yh_count
                from (
                    select yh_id,count(*)
                    from caozuo_jilu c
                    where c.caozuo=:operation
                    and c.riqi>=:date_begin
                    and c.riqi<=:date_end
                    group by yh_id,neirong
                ) as yh
                where yh.yh_id=u.id
            ) as counter
            from user as u
        '''
        param = {
            'operation': u'上传图片',
            'date_begin': date_begin,
            'date_end': date_end
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('statistics/tongji_time_slot.html',
            User=session['user_name'], rows=rows,
            date_begin=date_begin, date_end=date_end)

    def post(self):
        year_begin = request.form['year_begin']
        month_begin = request.form['month_begin']
        day_begin = request.form['day_begin']
        year_end = request.form['year_end']
        month_end = request.form['month_end']
        day_end = request.form['day_end']
        uri = '/tongji_time_slot?'
        uri += 'date_begin=%s-%s-%s' % (year_begin, month_begin, day_begin)
        uri += '&date_end=%s-%s-%s' % (year_end, month_end, day_end)
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


class InvokeMonth(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('login')
        date = datetime.datetime.now().strftime('%Y-%m')
        sql = '''
            select u.id,u.MingCheng,count(*)
            from user as u
            left join caozuo_jilu as c
            on c.yh_id=u.id
            where c.caozuo=:operation
            and locate(:date, c.riqi)>0
            group by u.id
        '''
        param = {
            'operation': u'打印',
            'date': date
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows_print = res.fetchall()
        res.close()
        param = {
            'operation': u'生成查询密码',
            'date': date
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows_code = res.fetchall()
        res.close()
        param = {
            'operation': u'导出到终端',
            'date': date
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows_export = res.fetchall()
        res.close()
        return render_template('statistics/invoke_month.html',
            User=session['user_name'], rows_print=rows_print, date=date,
            rows_code=rows_code, rows_export=rows_export)


class InvokeTimeSlot(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('login')
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        date_begin = request.args.get('date_begin', today)
        date_end = request.args.get('date_end', today)
        sql = '''
            select u.id,u.MingCheng,count(*)
            from user as u
            left join caozuo_jilu as c
            on c.yh_id=u.id
            where c.caozuo=:operation
            and c.riqi>=:date_begin
            and c.riqi<=:date_end
            group by u.id
        '''
        param = {
            'operation': u'打印',
            'date_begin': date_begin,
            'date_end': date_end
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows_print = res.fetchall()
        res.close()
        param = {
            'operation': u'生成查询密码',
            'date_begin': date_begin,
            'date_end': date_end
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows_code = res.fetchall()
        res.close()
        param = {
            'operation': u'导出到终端',
            'date_begin': date_begin,
            'date_end': date_end
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows_export = res.fetchall()
        res.close()
        return render_template('statistics/invoke_time_slot.html',
            User=session['user_name'], date_begin=date_begin,
            date_end=date_end, rows_print=rows_print,
            rows_code=rows_code, rows_export=rows_export)

    def post(self):
        year_begin = request.form['year_begin']
        month_begin = request.form['month_begin']
        day_begin = request.form['day_begin']
        year_end = request.form['year_end']
        month_end = request.form['month_end']
        day_end = request.form['day_end']
        date_begin = '%s-%s-%s' % (year_begin, month_begin, day_begin)
        date_end = '%s-%s-%s' % (year_end, month_end, day_end)
        return redirect('/invoke_time_slot?date_begin=%s&date_end=%s' % \
            (date_begin, date_end))


class InvokeLog(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('login')
        archieve_id = request.args.get('archieve_id', 0)
        sql = '''
            select d.id,d.danganhao,c.yh_id,c.caozuo,c.riqi,u.mingcheng
            from dangan as d
            left join caozuo_jilu as c
            on c.NeiRong=d.id
            left join user as u
            on c.yh_id=u.id
            where (c.CaoZuo=:operation_1
                or c.caozuo=:operation_2
                or c.caozuo=:operation_3)
            and d.danganhao=:archieve_id
        '''
        param = {
            'operation_1': u'打印',
            'operation_2': u'生成查询密码',
            'operation_3': u'导出到终端',
            'archieve_id': archieve_id
        }
        res = db_engine.execute(text(' '.join(sql.split())), param)
        rows = res.fetchall()
        res.close()
        return render_template('statistics/invoke_log.html',
            User=session['user_name'], rows=rows)

    def post(self):
        archieve_id = request.form['archieve_id']
        return redirect('/invoke_log?archieve_id=%s' % (archieve_id))
