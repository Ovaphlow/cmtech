# -*- coding=UTF-8 -*-
from flask import Flask, request, render_template
import globalvars
import index, daoru, luru, saomiao, shangchuan, dangan, test, controls
import tsgz, nglgw, chaxun_teshu, login
from werkzeug import secure_filename


app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'
app.config['UPLOAD_FOLDER'] = globalvars.G_UPLOAD_PATH


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        return login.post()
    else:
        return login.get()


@app.route('/logout')
def logout_page():
    return controls.logout()


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


@app.route('/shangchuan/<id>', methods=['POST', 'GET'])
def shangchuan_page(id):
    if request.method == 'POST':
        return shangchuan.post(id)
    else:
        return shangchuan.get(id)


@app.route('/dangan/<id>', methods=['POST', 'GET'])
def dangan_page(id):
    if request.method == 'POST':
        return  dangan.post(id)
    else:
        return dangan.get(id)


@app.route('/test', methods=['POST', 'GET'])
def test_page():
    if request.method == 'POST':
        return test.post()
    else:
        return test.get()


@app.route('/_upload_image_file', methods=['POST'])
def _upload_image_file():
    if request.method == 'POST':
        return controls.upload_image_file()


@app.route('/chaxun/tsgz', methods=['GET'])
def tsgz_page():
    return tsgz.get()


@app.route('/chaxun/nglgw', methods=['GET'])
def nglgw_page():
    return nglgw.get()


@app.route('/chaxun/dytx', methods=['GET'])
def dytx_pate():
    return chaxun_teshu.dytx_get()


if __name__ == '__main__':
    app.run()
