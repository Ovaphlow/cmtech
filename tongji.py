# -*- coding=UTF-8 -*-
from flask.views import MethodView

"""
统计
：各用户操作总数对比
：按月份各用户操作总数曲线
：按月份各用户扫描总数曲线
：按月份各用户添加档案总数曲线
"""

class TongJi(MethodView):
    def get(self):
        from flask import render_template, session
        from globalvars import connect_db, close_db

        if not 'user_id' in session:
            return redirect('/login')
        sql = '''
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
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return render_template('tongji.html',
            User = session['user_name'],
            counter_1 = result,
        )
