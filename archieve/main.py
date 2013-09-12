# -*- coding=UTF-8 -*-

from flask import Flask, request
import os
import globalvars
import index, daoru, luru, saomiao, shangchuan, dangan
from werkzeug import secure_filename

app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'
app.config['UPLOAD_FOLDER'] = globalvars.G_UPLOAD_PATH

@app.route('/', methods=['GET', 'POST'])
def index_page():
  if request.method == 'POST':
    return index.post()
  else:
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

@app.route('/saomiao', methods=['GET', 'POST'])
def saomiao_page():
  if request.method == 'POST':
    return saomiao.post()
  else:
    return saomiao.get()

@app.route('/shangchuan/<id>', methods=['GET', 'POST'])
def shangchuan_page(id, cat):
  if request.method == 'POST':
    return shangchuan.post(id)
  else:
    return shangchuan.get()

@app.route('/dangan/<id>')
def dangan_page(id):
  return dangan.get(id)

if __name__ == '__main__':
  app.run()
