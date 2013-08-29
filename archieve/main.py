# -*- coding=UTF-8 -*-
from flask import Flask, request
import os
import globalvars
import index, daoru, luru
from werkzeug import secure_filename

app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'
app.config['UPLOAD_FOLDER'] = globalvars.G_UPLOAD_PATH

@app.route('/')
def index_page():
  return index.get()

@app.route('/daoru', methods=['GET', 'POST'])
def daoru_page():
  if request.method == 'POST':
    return daoru.post()
  else:
    return daoru.get()

@app.route('/luru', methods=['GET', 'POST'])
def luru_page():
  if request.method == 'POST':
    return luru.post()
  else:
    return luru.get()

if __name__ == '__main__':
  app.run()
