# -*- coding=UTF-8 -*-
from flask import Flask, request
import os
import globalvars
import index, daoru, luru

app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'

@app.route('/')
def index_page():
  return index.get1()

@app.route('/daoru', methods=['get', 'post'])
def daoru_page():
  if request.method == 'get':
    return daoru.get()
  else:
    return daoru.post()

@app.route('/luru', methods=['get', 'post'])
def luru_page():
  if request.method == 'get':
    return luru.get()
  else:
    return luru.post()

if __name__ == '__main__':
  app.run()
