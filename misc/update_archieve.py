# -*- coding=UTF-8 -*-

from sqlalchemy import text, create_engine

# source是原档案号，target是新档案号
archieve = {'source': '03000097',
    'target': '030000971'}

cnx = {'user': 'root',
    'password': 'dsdfjk',
    'host': '127.0.0.1',
    'database': 'cm_archieve'}

cnx_dev = {'user': 'cmtech',
    'password': 'cmtech.1123',
    'host': '125.211.221.215',
    'database': 'cm_archieve'}

engine = create_engine('mysql+mysqlconnector://%s:%s@%s/%s' % \
    (cnx['user'], cnx['password'], cnx['host'], cnx['database']),
    pool_recycle=900, pool_size=1)


if __name__ == '__main__':
    sql = '''
        update dangan
        set danganhao=:archieve_target
        where danganhao=:archieve_source
    '''
    param = {'archieve_target': archieve['target'],
        'archieve_source': archieve['source']}
    engine.execute(text(' '.join(sql.split())), param)