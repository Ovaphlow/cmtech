# -*- coding=UTF-8 -*-

from sqlalchemy import create_engine

from archman import app

db_engine = create_engine('mysql+mysqlconnector://%s:%s@%s/%s' % (
    app.config['DB_USER'], app.config['DB_PASSWORD'], app.config['DB_HOST'],
    app.config['DB_NAME']), pool_recycle=60, pool_size=3)
