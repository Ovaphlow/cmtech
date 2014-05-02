# -*- coding=UTF-8 -*-

from flask import session, redirect, request, render_template
from flask.views import MethodView

from globalvars import connect_db, close_db, get_file_path


class SaoMiao(MethodView):
    def get(self, uid):
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
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        if cursor.rowcount > 0:
            row = data[0]
        else:
            row = None
        close_db(cursor, cnx)
        fp = get_file_path(uid)
        return render_template('saomiao.html',
            filepath = fp,
            row = row,
            id = uid,
            url_root = url_root,
            User = session['user_name'])

#     def post(self, uid):
#         pass
#         p = get_file_path1(id)
#         with open('d:\\11231.jpg', 'wb') as f:
#             f.write(request.data)
#         f.close()
#         return 'Received'
