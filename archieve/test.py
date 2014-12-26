# -*- coding=UTF-8 -*-
from flask.views import MethodView


class Test(MethodView):
    def get(self):
        from flask import render_template

        return render_template('test.html')

    def post(self):
        import os
        from flask import request
        from werkzeug import secure_filename

        import globalvars
        #print 'headers', request.headers
        id = request.args.get('id', '')
        #print 'id', id
        #print 'request.value', request.values
        aid = globalvars.get_aid(id)
        fp = '%s\\%s' % (globalvars.G_UPLOAD_PATH, aid)
        globalvars.check_path(fp)
        for f in request.files.getlist('Filedata'):
            if f and globalvars.check_ext(f.filename):
                fn = secure_filename(f.filename)
                fp = os.path.join(fp, fn)
                f.save(fp)
                return '[%s]上传完成' % (fn)
