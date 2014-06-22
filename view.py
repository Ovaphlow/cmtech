# -*- coding=UTF-8 -*-

from flask import redirect, render_template, session, request
from flask.views import MethodView

from globalvars import *


class Home(MethodView):
    def get(self):
        if not session['user_account'] in G_VIEW_USER:
            return redirect('/logout')
        return render_template('view_home.html', user_name=session['user_name'])