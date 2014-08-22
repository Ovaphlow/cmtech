# -*- coding=UTF-8 -*-

import settings

from sqlalchemy import create_engine

db_engine = create_engine('mysql+mysqlconnector://%s:%s@%s/%s' % (
    settings.db_user, settings.db_password, settings.db_host,
    settings.db_name), pool_recycle=900, pool_size=3)
