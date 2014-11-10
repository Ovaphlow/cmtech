# -*- coding=UTF-8 -*-


class Config(object):
    DEBUG = False
    SECRET_KEY = '8124uckmbUYIj3wr7*)(935okk)'

    PORT = 8000

    NGINX_URL = '//localhost:8080/'
    NGINX_PATH = 'd:\\srcode\\web_public'

    FILE_DIR = 'archman'
    FILE_EXT = '.jpg'

    DB_USER = 'cmtech'
    DB_PASSWORD = 'cmtech.1123'
    DB_HOST = '125.211.221.215'
    DB_NAME = 'archman'


class DevelopmentConfig(Config):
    DEBUG = True
