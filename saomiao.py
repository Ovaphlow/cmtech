# -*- coding=UTF-8 -*-
from flask.views import MethodView


class SaoMiao(MethodView):
    def get(self, uid):
        from flask import session, redirect, request, render_template
        import globalvars
#         import mysql.connector

        if not 'user_id' in session:
            return redirect('/login')
        url_root = request.url_root
        sql = '''
            SELECT * FROM dangan
            WHERE id=%s
        '''
        param = (
            uid,
        )
#         cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cnx = globalvars.connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if cursor.rowcount > 0:
            row = data[0]
        else:
            row = None
#         cursor.close()
#         cnx.close()
        globalvars.close_db(cursor, cnx)
        fp = globalvars.get_file_path(uid)
        return render_template(
            'saomiao.html',
            filepath = fp,
            row = row,
            id = uid,
            url_root = url_root,
            User = session['user_name']
        )

    def post(self, uid):
        pass
#         import globalvars
#         from flask import request
#
#         p = globalvars.get_file_path1(id)
#         with open('d:\\11231.jpg', 'wb') as f:
#             f.write(request.data)
#         f.close()
#         return 'Received'
