# -*- coding=UTF-8 -*-
from flask import request, render_template
from werkzeug import secure_filename
import main
import globalvars
import time
import os


def get():
    return render_template('test.html')


def post():
    id = request.args.get('id', '')
    cat = request.args.get('cat', '')
    aid = globalvars.get_aid(id)
    fp = '%s\\%s' % (globalvars.G_UPLOAD_PATH, aid)
    globalvars.check_path(fp)
    file_time = time.localtime()
    file_name = '%s.jpg' % (time.strftime('%Y%m%d%H%M%S', file_time))
    fp = '%s\\%s' % (fp, file_name)
    with open(fp, 'wb') as f:
        f.write(request.data)
    f.close()
    return '完成'

if __name__ == '__main__':
    import Image
    import os
    img = Image.open('1.jpg')
    print img.format, img.size, img.mode
    im = img.transpose(Image.ROTATE_270)
    im.save('1.jpg')
