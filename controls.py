# -*- coding=UTF-8 -*-
from flask.views import MethodView


class UploadImageFile(MethodView):
    def post(self):
        from flask import request, session
        import datetime
        import globalvars

        rec_id = request.args.get('id', '')
        cat = request.args.get('cat', '1')
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
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        cnx.commit()
        globalvars.close_db(cursor, cnx)
        globalvars.rotate_image(fp)
        globalvars.caozuo_jilu(session['id'], u'上传图片', fp)
        return '完成'


class GenCode(MethodView):
    def get(self, archieve_id):
        from flask import redirect
        from globalvars import connect_db, close_db
        from random import randint
        import datetime

        code = randint(1000, 9999)
        date = datetime.datetime.now()
        sql = '''
            SELECT shenfenzheng FROM dangan
            WHERE id=%(archieve_id)s
        '''
        param = {'archieve_id': archieve_id,}
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        sql = '''
            INSERT INTO access_code (
                archieve_id, code, date
            )
            VALUES(
                %(archieve_id)s, %(code)s, %(date)s
            )
        '''
        param = {
            'archieve_id': result[0][0],
            'code': code,
            'date': date.strftime('%Y-%m-%d'),
        }
        cursor.execute(sql, param)
        cnx.commit()
        close_db(cursor, cnx)
        return redirect('/dangan/%s' % archieve_id)


def render_text(file_name, font_size, text, output_name, output_type):
    from PIL import Image, ImageDraw, ImageFont

    img = Image.open(file_name)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('c:\\windows\\fonts\\simhei.ttf', font_size)
    draw.text((10, 20), text, font=font, fill=(255,0,0,255))
    img.save(output_name, output_type)
    #img.show()
