# -*- coding=UTF-8 -*-

from flask import Flask, request
import os
import globalvars
import index, daoru, luru, saomiao, shangchuan, dangan, test, controls
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

@app.route('/saomiao/<id>', methods=['GET', 'POST'])
def saomiao_page(id):
  if request.method == 'POST':
    return saomiao.post(id)
  else:
    return saomiao.get(id)

@app.route('/_shangchuan', methods=['POST', 'GET'])
def _shangchuan_page():
  if request.method == 'POST':
    return controls._shangchuan()

@app.route('/shangchuan/<id>', methods=['GET'])
def shangchuan_page(id):
  return shangchuan.get(id)

@app.route('/dangan/<id>')
def dangan_page(id):
  return dangan.get(id)

@app.route('/test')
def test_page():
  return test.get()

if __name__ == '__main__':
  app.run()
