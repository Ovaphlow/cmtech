# -*- coding=UTF-8 -*-
from flask import render_template, redirect, session


def get(pic_id):
    if not 'id' in session:
        return redirect('/login')
    return render_template('dangan.html')


def post(pic_id):
    pass