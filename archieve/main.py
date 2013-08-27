# -*- coding=UTF-8 -*-
from flask import Flask, request
import os
import globalvars
import index

app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'

@app.route('/')
def index_page():
  return index.run()

if __name__ == '__main__':
  app.run()
