# -*- coding=UTF-8 -*-

import globalvars
import mysql.connector
from flask import request, render_template, redirect
from werkzeug import secure_filename

def get(id):
    return render_template('saomiao.html', path=id, filepath=globalvars.G_LOCAL_PATH)

def post(id):
    return redirect('/shangchuan/%s' % (id))
