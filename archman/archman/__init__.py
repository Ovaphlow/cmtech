# -*- coding=UTF-8 -*-

from flask import Flask

app = Flask(__name__)

app.config.from_object('archman.config.DevelConfig')

from archman import home
from archman import archive
