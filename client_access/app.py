# -*- coding=UTF-8 -*-
from flask import Flask
import index, archieve

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
app.add_url_rule(
    '/archieve',
    view_func = archieve.Archieve.as_view('archieve')
)
app.add_url_rule(
    '/view',
    view_func = archieve.View.as_view('view')
)
app.add_url_rule(
    '/view_cat/<cat>',
    view_func = archieve.ViewCat.as_view('view_cat')
)


if __name__ == '__main__':
    app.run(port = 5001)
