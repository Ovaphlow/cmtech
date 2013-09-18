# -*- coding=UTF-8 -*-

from flask import Flask, request, render_template
import os
import globalvars
from werkzeug import secure_filename

app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'
app.config['UPLOAD_FOLDER'] = globalvars.G_UPLOAD_PATH

@app.route('/', methods=['GET', 'POST'])
def index_page():
  if request.method == 'POST':
    return render_template('index_hpdw.html')
  else:
    return render_template('index_hpdw.html')

if __name__ == '__main__':
  app.run()
