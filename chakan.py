# -*- coding=UTF-8 -*-


def get(pic_id):
    from flask import session, redirect, render_template
    import mysql.connector
    import globalvars

    if not 'id' in session:
        return redirect('/login')
    sql = '''
        SELECT wenjian.id,wenjian.aid,wenjian.wenjianming,dangan.danganhao
        FROM wenjian INNER JOIN dangan ON wenjian.aid=dangan.id
        WHERE wenjian.id=%s
    '''
    param = (pic_id,)
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchall()
    cursor.close()
    cnx.close()
    row = data[0]
    return render_template('chakan.html',
                           fs_root=globalvars.G_FILE_SERVER_ROOT,
                           aid=row[3],
                           row=row
    )


def post(pic_id):
    from flask import redirect
    import mysql.connector
    import globalvars

    sql = '''
        SELECT wenjian.id,wenjian.aid,wenjian.wenjianming,dangan.danganhao
        FROM wenjian INNER JOIN dangan ON wenjian.aid=dangan.id
        WHERE wenjian.id=%s
    '''
    param = (pic_id,)
    cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
    cursor = cnx.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchall()
    cursor.close()
    cnx.close()
    row = data[0]
    ret = globalvars.turn_image('%s\%s\%s' % (globalvars.G_UPLOAD_PATH,
                                              row[3],
                                              row[2]
                                             )
                               )
    return redirect('/chakan/%s' % pic_id)