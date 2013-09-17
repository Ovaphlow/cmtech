# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
import os
from flask import request, render_template, redirect
from werkzeug import secure_filename

def _shangchuan():
  if request.method == 'POST':
    files_list = request.files.getlist('file1')
    for f in files_list:
      if f and globalvars.check_ext(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
    files_list = request.files.getlist('file2')
    for f in files_list:
      if f and globalvars.check_ext(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
    files_list = request.files.getlist('file3')
    for f in files_list:
      if f and globalvars.check_ext(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
    files_list = request.files.getlist('file4')
    for f in files_list:
      if f and globalvars.check_ext(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
    files_list = request.files.getlist('file5')
    for f in files_list:
      if f and globalvars.check_ext(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
    files_list = request.files.getlist('file6')
    for f in files_list:
      if f and globalvars.check_ext(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
    files_list = request.files.getlist('file7')
    for f in files_list:
      if f and globalvars.check_ext(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
    files_list = request.files.getlist('file8')
    for f in files_list:
      if f and globalvars.check_ext(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
    files_list = request.files.getlist('file9')
    for f in files_list:
      if f and globalvars.check_ext(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(globalvars.G_UPLOAD_PATH, filename))
    return redirect('/')
