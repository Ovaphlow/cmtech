# -*- coding=UTF-8 -*-
from flask.views import MethodView


class TongJi(MethodView):
    def get(self):
        from flask import render_template, session, redirect

        if not 'user_id' in session:
            return redirect('/login')

        return render_template('tongji.html', User = session['user_name'])

