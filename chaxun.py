# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import render_template, request, redirect, session, escape


def get():
    return render_template('chaxun.html')


def post():
    print request.form['DangAnHao']
    print request.form['ShenFenZheng']
    print request.form['XingMing']
    print request.form['XingBie']
    return render_template('chaxun.html')