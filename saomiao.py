# -*- coding=UTF-8 -*-

from flask import session, redirect, request, render_template
from flask.views import MethodView

from globalvars import connect_db, close_db, get_file_path


