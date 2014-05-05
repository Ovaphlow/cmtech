# -*- coding=UTF-8 -*-

from flask import redirect, render_template, session, request
from flask.views import MethodView

from globalvars import connect_db, close_db, G_ADMIN_USER


class Index(MethodView):
    def get(self):
        if not 'user_id' in session:
            return redirect('/login')
        sql = 'select count(*) from dangan'
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql)
        data_count1 = cursor.fetchall()
        sql = '''
            select count(*)
            from (
                select d.id
                from dangan d
                inner join wenjian w
                on d.id=w.aid
                group by d.id
            ) as a
        '''
        cursor.execute(sql)
        data_count2 = cursor.fetchall()
        sql = 'select count(*) from wenjian'
        cursor.execute(sql)
        data_count3 = cursor.fetchall()
        sql = '''
            select caozuo, count(*)
            from caozuo_jilu
            where yh_id=%(user_id)s
            group by caozuo
        '''
        param = {'user_id': session['user_id']}
        cursor.execute(sql, param)
        result = cursor.fetchall()
        close_db(cursor, cnx)
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
        return render_template('index.html',
            User=session['user_name'],
            data_count1=data_count1,
            data_count2=data_count2,
            data_count3=data_count3,
            opr_count1=opr_count1,
            opr_count2=opr_count2,
            opr_count3=opr_count3,
            opr_count4=opr_count4)

    def post(self):
        sql = '''
            select id
            from dangan
            where DangAnHao=%(archieve_id)s
            or ShenFenZheng=%(id_card)s
        '''
        param = {
            'archieve_id': request.form['id'],
            'id_card': request.form['id']
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if cursor.rowcount == 0:
            return redirect('/luru')
        else:
            return redirect('/dangan/' + str(data[0][0]))


class Login(MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        _acc = request.form['zhanghao']
        _pwd = request.form['mima']
        cnx = connect_db()
        cursor = cnx.cursor()
        sql = '''
            select count(*),id,zhanghao,MingCheng
            from user
            where ZhangHao=%(account)s
            and MiMa=%(password)s
        '''
        param = {
            'account': _acc,
            'password': _pwd
        }
        cursor.execute(sql, param)
        data = cursor.fetchall()
        close_db(cursor, cnx)
        if data[0][0] == 1:
            session['user_id'] = data[0][1]
            session['user_account'] = data[0][2]
            session['user_name'] = data[0][3]
            if data[0][2] in G_ADMIN_USER:
                return redirect('/admin')
            else:
                return redirect('/')
        else:
            return redirect('/login')


class Logout(MethodView):
    def get(self):
        session.pop('user_id', None)
        session.pop('user_account', None)
        session.pop('user_name', None)
        return redirect('/login')
