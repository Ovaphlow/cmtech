# -*- coding=UTF-8 -*-

import settings

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


def run():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(settings.port)
    IOLoop.instance().start()


if __name__ == '__main__':
    run()
