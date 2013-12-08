# -*- coding=UTF-8 -*-
from flask.views import MethodView


class Logout(MethodView):
    def get(self):
        from flask import session, redirect

        session.pop('id', None)
        session.pop('user', None)
        return redirect('/login')


class UploadImageFile(MethodView):
    def post(self):
        from flask import request, session
        from werkzeug import secure_filename
        import datetime
        import mysql.connector
        import globalvars

        id = request.args.get('id', '')
        cat = request.args.get('cat', '')
        aid = globalvars.get_aid(id)
        fp = '%s\\%s' % (globalvars.G_UPLOAD_PATH, aid)
        globalvars.check_path(fp)
        file_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        file_name = '%s.jpg' % (file_time)
        fp = '%s\\%s' % (fp, file_name)
        with open(fp, 'wb') as f:
            f.write(request.data)
        f.close()
        sql = '''
            INSERT INTO wenjian
            (aid, LeiBie, WenJianMing)
            VALUES(%s, %s, %s)
        '''
        param = (id, cat, file_name)
        cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        cnx.commit()
        cursor.close()
        cnx.close()
        globalvars.rotate_image(fp)
        globalvars.caozuo_jilu(session['id'], u'上传图片', fp)
        return '完成'
