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