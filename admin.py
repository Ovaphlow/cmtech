# -*- coding=UTF-8 -*-

from flask import redirect, render_template, session, request
from flask.views import MethodView

from globalvars import connect_db, close_db, G_ADMIN_USER


class Home(MethodView):
    def get(self):
        if not session['user_account'] in G_ADMIN_USER:
            return redirect('/logout')
        return render_template('admin_home.html',
            user_name=session['user_name'])


class UserList(MethodView):
    def get(self):
        if not session['user_account'] in G_ADMIN_USER:
            return redirect('/logout')
        sql = '''
            select *
            from user
        '''
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(' '.join(sql.split()))
        res = cursor.fetchall()
        return render_template('admin_user_list.html',
            user_name=session['user_name'],
            data=res)


class User(MethodView):
    def get(self):
        if not session['user_account'] in G_ADMIN_USER:
            return redirect('/logout')
        user_id = request.args.get('user_id')
        sql = '''
            select *
            from user
            where id=%(user_id)s
        '''
        param = {'user_id': user_id}
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(' '.join(sql.split()), param)
        res = cursor.fetchall()
        close_db(cursor, cnx)
        if not res:
            return redirect('/admin')
        return render_template('admin_user.html',
            row=res[0],
            user_name=session['user_name'])

    def post(self):
        user_id = request.args.get('user_id')
        sql = '''
            update user
            set
                MingCheng=%(name)s,ZhangHao=%(account)s,MiMa=%(pwd)s
            where
                id=%(user_id)s
        '''
        param = {
            'name': request.form['name'],
            'account': request.form['account'],
            'pwd': request.form['password'],
            'user_id': user_id
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(' '.join(sql.split()), param)
        cnx.commit()
        close_db(cursor, cnx)
        return redirect('/admin/user?user_id=%s' % (user_id))


class AddUser(MethodView):
    def get(self):
        if not session['user_account'] in G_ADMIN_USER:
            return redirect('/logout')
        _err = request.args.get('err', '0')
        if _err == '1':
            _err_message = u'姓名不能为空'
        elif _err == '2':
            _err_message = u'账号不能为空'
        elif _err == '3':
            _err_message = u'密码不能为空'
        else:
            _err_message = None
        return render_template('admin_add_user.html',
            user_name=session['user_name'],
            error=_err_message)

    def post(self):
        _name = request.form['name']
        _account = request.form['account']
        _password = request.form['password']
        if not _name:
            return redirect('/admin/add_user?err=1')
        if not _account:
            return redirect('/admin/add_user?err=2')
        if not _password:
            return redirect('/admin/add_user?err=3')
        sql = '''
            insert into user
                (ZhangHao,Mima,MingCheng)
            values
                (%(account)s,%(password)s,%(name)s)
        '''
        param = {
            'account': _account,
            'password': _password,
            'name': _name
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(' '.join(sql.split()), param)
        cnx.commit()
        close_db(cursor, cnx)
        return redirect('/admin/user_list')