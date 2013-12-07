# -*- coding=UTF-8 -*-
from flask.views import MethodView


class XiuGaiMiMa(MethodView):
    def get(self):
        from flask import render_template

        return render_template('xgmm.html')

    def post(self):
        from flask import redirect

        return redirect('/xgmm')