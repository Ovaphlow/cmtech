# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
import os
from flask import request, render_template
from werkzeug import secure_filename

def get(id):
  return render_template('shangchuan.boot.html', id=id)
