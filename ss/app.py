# -*- coding=UTF-8 -*-
from flask import Flask

import chart


app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'
app.add_url_rule(
    '/chart',
    view_func = chart.Chart.as_view('chart')
)

if __name__ == '__main__':
    app.run()
