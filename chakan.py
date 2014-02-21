# -*- coding=UTF-8 -*-
from flask.views import MethodView


class ChaKan(MethodView):
    def get(self, rec_id):
        from flask import session, redirect, render_template, request
        import globalvars

        if not 'user_id' in session:
            return redirect('/login')
        pic_id = request.args.get('pic_id', '0')
        sql = '''
            SELECT wenjian.id,wenjian.aid,wenjian.wenjianming,
                dangan.danganhao,wenjian.client_access
            FROM wenjian INNER JOIN dangan ON wenjian.aid=dangan.id
            WHERE wenjian.id=%s
        '''
        param = (pic_id,)
        sql_t = '''
            select id
            from `cm_archieve`.wenjian
            where id = (
                select max(id)
                from wenjian
                where id<%(rec_id)s
                and aid=%(archieve_id)s
            ) or id = (
                select min(id)
                from wenjian
                where id>%(rec_id)s
                and aid=%(archieve_id)s
            )
        '''
        param_t = {
            'archieve_id': rec_id,
            'rec_id': pic_id
        }
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        cursor.execute(sql_t, param_t)
        result = cursor.fetchall()
        if cursor.rowcount == 0:
            previous_id = None
            next_id = None
        else:
            if int(result[0][0]) < int(pic_id):
                previous_id = result[0][0]
                if len(result) == 2:
                    previous_id = result[0][0]
                    next_id = result[1][0]
                else:
                    next_id = None
            else:
                previous_id = None
                next_id = result[0][0]
        globalvars.close_db(cursor, cnx)
        row = data[0]
        return render_template(
            'chakan.html',
            fs_root = globalvars.G_FILE_SERVER_ROOT,
            aid = row[3],
            row = row,
            User = session['user_name'],
            archieve_id = rec_id,
            previous_id = previous_id,
            next_id = next_id,
            pic_id = pic_id
        )

    def post(self, rec_id):
        from flask import redirect, request
        import globalvars
        import os

        opr = request.form['operate']
        pic_id = request.args.get('pic_id', '')
        if opr == 'turn':
            sql = '''
                SELECT w.id,w.aid,w.wenjianming,d.danganhao
                FROM wenjian w INNER JOIN dangan d ON w.aid=d.id
                WHERE w.id=%s
            '''
            param = (pic_id,)
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            row = data[0]
            globalvars.turn_image(
                '%s\%s\%s' % \
                (globalvars.G_UPLOAD_PATH, row[3], row[2])
            )
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'rotate':
            sql = '''
                SELECT w.id,w.aid,w.wenjianming,d.danganhao
                FROM wenjian w INNER JOIN dangan d ON w.aid=d.id
                WHERE w.id=%s
            '''
            param = (pic_id,)
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            row = data[0]
            globalvars.rotate_image(
                '%s\%s\%s' % \
                (globalvars.G_UPLOAD_PATH, row[3], row[2])
            )
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'delete':
            sql = '''
                SELECT w.id,w.aid,w.wenjianming,d.danganhao
                FROM wenjian w INNER JOIN dangan d ON w.aid=d.id
                WHERE w.id=%s
            '''
            param = (pic_id,)
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            sql = 'DELETE FROM wenjian WHERE id=%s'
            param = (pic_id,)
            cursor.execute(sql, param)
            cnx.commit()
            row = data[0]
            fp = '%s\%s\%s' % (globalvars.G_UPLOAD_PATH, row[3], row[2])
            if os.path.isfile(fp):
                os.remove(fp)
            globalvars.close_db(cursor, cnx)
            return redirect('/dangan/%s' % rec_id)
        elif opr == 'access':
            sql = '''
                UPDATE wenjian
                SET client_access=%(client_access)s
                WHERE id=%(pic_id)s
            '''
            param = {
                'client_access': 1,
                'pic_id': pic_id,
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'cancel_access':
            sql = '''
                UPDATE wenjian
                SET client_access=%(client_access)s
                WHERE id=%(pic_id)s
            '''
            param = {
                'client_access': 0,
                'pic_id': pic_id,
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat1':
            sql = ('update '
                'wenjian '
                'set '
                'leibie=1 '
                'where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat2':
            sql = ('update wenjian set leibie=2 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat3':
            sql = ('update wenjian set leibie=3 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat4':
            sql = ('update wenjian set leibie=4 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat5':
            sql = ('update wenjian set leibie=5 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat6':
            sql = ('update wenjian set leibie=6 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat7':
            sql = ('update wenjian set leibie=7 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat8':
            sql = ('update wenjian set leibie=8 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        elif opr == 'movetocat9':
            sql = ('update wenjian set leibie=9 where '
                'id=%(pic_id)s')
            param = {
                'pic_id': pic_id
            }
            cnx = globalvars.connect_db()
            cursor = cnx.cursor()
            cursor.execute(sql, param)
            cnx.commit()
            globalvars.close_db(cursor, cnx)
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))
        else:
            return redirect('/chakan/%s?pic_id=%s' % (rec_id, pic_id))


class DaYin(MethodView):
    def get(self, archieve_id):
        from globalvars import render_text, connect_db, close_db, G_UPLOAD_PATH
        from flask import request, redirect

        pic_id = request.args.get('pic_id')
        if pic_id == '':
            redirect('/')
        sql = ('select '
            'd.DangAnHao, ( '
            'select '
            'w.WenJianMing '
            'from '
            'cm_archieve.wenjian w '
            'where '
            'w.id=%(pic_id)s '
            'and '
            'w.aid=d.id '
            ') as pic_name '
            'from '
            'cm_archieve.dangan d '
            'where '
            'd.id=%(archieve_id)s')
        param = {
            'pic_id': request.args.get('pic_id'),
            'archieve_id': archieve_id
        }
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        close_db(cursor, cnx)
        file_name = '%s\%s\%s' % (G_UPLOAD_PATH, result[0][0], result[0][1])
        render_text(
            file_name=file_name,
            font_size=32,
            text=u'与原件相符',
            output_name='%s/%s/for_print.png' % (G_UPLOAD_PATH, result[0][0]),
            output_type='png'
        )
        return '<img src="/static/upload/%s/for_print.png" />' % \
            (result[0][0])