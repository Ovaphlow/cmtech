# -*- coding=UTF-8 -*-
from flask import Flask
import index

app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'
app.add_url_rule(
    '/',
    view_func = index.Index.as_view('index')
)
app.add_url_rule(
    '/code',
    view_func = index.Code.as_view('code')
)


if __name__ == '__main__':
    app.run(port = 5001)
