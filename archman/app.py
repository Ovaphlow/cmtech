# -*- coding=UTF-8 -*-

from archman import app

app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
