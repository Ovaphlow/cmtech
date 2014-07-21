# -*- coding=UTF-8 -*-

from flask import redirect, render_template, session, request
from flask.views import MethodView
from sqlalchemy import text

from globalvars import *


class Home(MethodView):
    def get(self):
        if not session['user_account'] in G_ADMIN_USER:
            return redirect('/logout')
        sql = '''
            select l.riqi,l.shijian,u.mingcheng,l.caozuo,a.danganhao
            from caozuo_jilu as l,
                user as u,
                dangan as a
            where l.yh_id=u.id
            and l.neirong=a.id
            order by l.id desc
            limit 100
        '''
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(' '.join(sql.split()))
        res = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template('admin/home.html',
            user_name=session['user_name'],
            data=res)


class UserList(MethodView):
    def get(self):
        if not session['user_account'] in G_ADMIN_USER:
            return redirect('/logout')
        sql = '''
            select *
            from user
        '''
        res = db_engine.execute(text(' '.join(sql.split())))
        rows = res.fetchall()
        res.close()
        return render_template('admin/user_list.html',
            user_name=session['user_name'],
            data=rows)


class AuthDelArchieve(MethodView):
    def get(self):
        if not session['user_account'] in G_ADMIN_USER:
            return redirect('/logout')
        user_id = request.args.get('user_id')
        sql = '''
            select *
            from user
            where id=:id
        '''
        param = {'id': user_id}
        res = db_engine.execute(text(' '.join(sql.split())), param)
        row = res.fetchone()
        res.close()
        sql = '''
            update user
            set auth_del_archieve=:auth
            where id=:user_id
        '''
        if row.auth_del_archieve:
            param = {'auth': 0,
                'user_id': user_id}
        else:
            param = {'auth': 1,
                'user_id': user_id}
        db_engine.execute(text(' '.join(sql.split())), param)
        return redirect('/admin/user_list')


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
        return render_template('admin/user.html',
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
        return render_template('admin/add_user.html',
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


class Archieve(MethodView):
    def get(self):
        if not session['user_account'] in G_ADMIN_USER:
            return redirect('/logout')
        archieve_id = request.args.get('archieve_id')
        id_card = request.args.get('id_card')
        name = request.args.get('name')
        sql = '''
            select *
            from dangan
            where zhuanchu is null
            or zhuanchu=""
        '''
        if archieve_id:
            sql += '''
                and locate(%(archieve_id)s,danganhao) > 0
            '''
        if id_card:
            sql += '''
                and locate(%(id_card)s, shenfenzheng) > 0
            '''
        if name:
            sql += '''
                and locate(%(name)s, xingming) > 0
            '''
        sql += '''
            limit 20
        '''
        param = {
            'archieve_id': archieve_id,
            'id_card': id_card,
            'name': name
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(' '.join(sql.split()), param)
        res = cursor.fetchall()
        close_db(cursor, cnx)
        return render_template('admin/archieve.html',
            user_name=session['user_name'],
            data=res)

    def post(self):
        archieve_id = request.form['archieve_id']
        id_card = request.form['id_card']
        name = request.form['name']
        url = '/admin/archieve?archieve_id=%s&id_card=%s&name=%s' % \
            (archieve_id, id_card, name)
        return redirect(url)


class DeleteArchieve(MethodView):
    def get(self):
        archieve_id = request.args.get('archieve_id')
        if not archieve_id:
            return redirect('/admin')
        sql = '''
            delete
            from dangan
            where id=%(archieve_id)s
        '''
        param = {'archieve_id': archieve_id}
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(' '.join(sql.split()), param)
        cnx.commit()
        close_db(cursor, cnx)
        return redirect('/admin/archieve')
