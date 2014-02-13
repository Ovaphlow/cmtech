# -*- coding=UTF-8 -*-
from flask.views import MethodView
#http://localhost:5000/chart?type=column&height=200&title=中&subtitle=中文&name=a,b,c&value=11,41,27"""
"""
统计
：各用户操作总数对比
：按月份各用户操作总数曲线
：按月份各用户扫描总数曲线
：按月份各用户添加档案总数曲线
"""

class Chart(MethodView):
    def get(self):
        from flask import render_template, session, request
        import sys

        reload(sys)
        sys.setdefaultencoding('utf-8')
        name = request.args.get('name')
        value = request.args.get('value')
        name = name.split(',')
        value = value.split(',')
        print request.args.get('title')
        return render_template(
            'chart.html',
            type = request.args.get('type', 'column'),
            height = request.args.get('height', '300'),
            title = request.args.get('title'),
            subtitle = request.args.get('subtitle'),
            name = name,
            count_name = len(name),
            value = value,
            count_value = len(value)
        )
