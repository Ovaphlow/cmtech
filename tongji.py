# -*- coding=UTF-8 -*-
from flask.views import MethodView

#统计
#：各用户操作总数对比
#：按月份各用户操作总数曲线
#：按月份各用户扫描总数曲线
#：按月份各用户添加档案总数曲线


class TongJi(MethodView):
    def get(self):
        from flask import render_template, session
        from globalvars import connect_db, close_db
        import datetime

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
        from flask import render_template, session, request
        from globalvars import connect_db, close_db
        import datetime

        if not 'user_id' in session:
            return redirect('/login')
        _year = request.args.get('year', datetime.datetime.now().strftime('%Y'))
        _month = request.args.get('month', datetime.datetime.now().strftime('%m'))
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
        from flask import request, redirect

        year = request.form['year']
        month = request.form['month']

        return redirect('/tongji_month/?year=%s&month=%s' % (year, month))
