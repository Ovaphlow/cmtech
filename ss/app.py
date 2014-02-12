# -*- coding=UTF-8 -*-
from flask import Flask

import globalvars
import index
import controls
import tongji


app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'
app.add_url_rule(
    '/',
    view_func = index.Index.as_view('index')
)
app.add_url_rule(
    '/tongji',
    view_func = tongji.TongJi.as_view('tong_ji')
)

if __name__ == '__main__':
    app.run()
