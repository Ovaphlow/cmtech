# -*- coding=UTF-8 -*-
from flask import Flask

import globalvars
import index
import daoru
import luru
import saomiao
import shangchuan
import dangan
import controls
import login
import chakan
import chaxun


app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'
app.config['UPLOAD_FOLDER'] = globalvars.G_UPLOAD_PATH
app.add_url_rule('/', view_func=index.Index.as_view('index'))
app.add_url_rule('/login', view_func=login.Login.as_view('login'))
app.add_url_rule('/logout', view_func=controls.Logout.as_view('logout'))
app.add_url_rule('/chaxun', view_func=chaxun.ChaXun.as_view('chaxun'))
app.add_url_rule('/chakan/<pic_id>', view_func=chakan.ChaKan.as_view('chakan'))
app.add_url_rule('/daoru', view_func=daoru.DaoRu.as_view('daoru'))
app.add_url_rule('/luru', view_func=luru.LuRu.as_view('luru'))
app.add_url_rule('/saomiao/<id>', view_func=saomiao.SaoMiao.as_view('saomiao'))
app.add_url_rule('/shangchuan/<id>', view_func=shangchuan.ShangChuan.as_view('shangchuan'))
app.add_url_rule('/dangan/<id>', view_func=dangan.DangAn.as_view('dangan'))
app.add_url_rule('/_upload_image_file', view_func=controls.UploadImageFile.as_view('ulpic'))
app.add_url_rule('/chaxun/tsgz', view_func=chaxun.TeShuGongZhong.as_view('tsgz'))
app.add_url_rule('/chaxun/nglgw', view_func=chaxun.NvGuanLiGangWei.as_view('nglgw'))
app.add_url_rule('/chaxun/dytx', view_func=chaxun.DangYueTuiXiu.as_view('dytx'))

if __name__ == '__main__':
    app.run()
