# -*- coding=UTF-8 -*-
from flask.views import MethodView


class UploadImageFile(MethodView):
    def post(self):
        from flask import request, session
        import datetime
        import globalvars 

        rec_id = request.args.get('id', '')
        cat = request.args.get('cat', '')
        aid = globalvars.get_aid(rec_id)
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
        param = (rec_id, cat, file_name)
#         cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        cnx.commit()
#         cursor.close()
#         cnx.close()
        globalvars.close_db(cursor, cnx)
        globalvars.rotate_image(fp)
        globalvars.caozuo_jilu(session['id'], u'上传图片', fp)
        return '完成'
