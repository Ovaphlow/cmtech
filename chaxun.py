# -*- coding=UTF-8 -*-
from flask.views import MethodView


class ChaXun(MethodView):
    def get(self):
        from flask import render_template

        return render_template('chaxun.html')

    def post(self):
        from flask import request, render_template

        print request.form['DangAnHao']
        print request.form['ShenFenZheng']
        print request.form['XingMing']
        print request.form['XingBie']
        return render_template('chaxun.html')
