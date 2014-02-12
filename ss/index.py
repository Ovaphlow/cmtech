# -*- coding=UTF-8 -*-
from flask.views import MethodView


class Index(MethodView):
    def get(self):
        import mysql.connector
        from flask import redirect, render_template, session
        import globalvars

        if not 'user_id' in session:
            return redirect('/login')
        sql = '''
            SELECT COUNT(*) FROM dangan
            UNION
            SELECT COUNT(*) FROM (
                SELECT d.id
                FROM dangan d
                INNER JOIN wenjian w
                ON d.id=w.aid
                GROUP BY d.id
            ) AS a
            UNION
            SELECT COUNT(*) FROM wenjian
        '''
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data_count = cursor.fetchall()
        sql = '''
            select
                caozuo, count(*)
            from
                caozuo_jilu
            where
                yh_id=%(user_id)s
            group by
                caozuo
        '''
        param = {'user_id': session['user_id']}
        cursor.execute(sql, param)
        result = cursor.fetchall()
        globalvars.close_db(cursor, cnx)
        opr_count1 = 0
        opr_count2 = 0
        opr_count3 = 0
        opr_count4 = 0
        for row in result:
            if row[0] == u'添加档案信息':
                opr_count1 = row[1]
            elif row[0] == u'修改档案信息':
                opr_count2 = row[1]
            elif row[0] == u'上传图片':
                opr_count3 = row[1]
            elif row[0] == u'批量上传':
                opr_count4 = row[1]
        return render_template(
            'index.html',
            User = session['user_name'],
            data_count = data_count,
            opr_count1 = opr_count1,
            opr_count2 = opr_count2,
            opr_count3 = opr_count3,
            opr_count4 = opr_count4,
        )
