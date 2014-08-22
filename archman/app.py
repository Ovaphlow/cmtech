# -*- coding=UTF-8 -*-

from flask import Flask

import archive
import home
import settings


app = Flask(__name__)
app.config.from_object('app.settings')

app.add_url_rule('/', view_func=home.Home.as_view('home'))
app.add_url_rule('/login', view_func=home.Login.as_view('login'))
app.add_url_rule('/logout', view_func=home.Login.as_view('logout'))

app.add_url_rule('/archive', view_func=archive.Archive.as_view('archive'))


if __name__ == '__main__':
    app.run(port=settings.port)
