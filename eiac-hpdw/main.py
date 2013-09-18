# -*- coding=UTF-8 -*-

from flask import Flask, request, render_template, redirect, session
import os
import globalvars
from werkzeug import secure_filename

app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'
app.config['UPLOAD_FOLDER'] = globalvars.G_UPLOAD_PATH

@app.route('/', methods=['POST', 'GET'])
def root():
  if 'uid' in session:
    return render_template('index.html')
  return redirect('/login')

@app.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    session['uid'] = request.form['account']
    return redirect('/')
  else:
    return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('uid', None)
  return redirect('/login')

if __name__ == '__main__':
  app.run()
