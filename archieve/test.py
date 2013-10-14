# -*- coding=UTF-8 -*-

from flask import request, render_template
from werkzeug import secure_filename
import main

def get():
    return render_template('test.html')

def post():
    #print request.data
    import os
    with open('d:\\11231.jpg', 'wb') as f:
        f.write(request.data)
    f.close()
    return 'Received: ' + request.data