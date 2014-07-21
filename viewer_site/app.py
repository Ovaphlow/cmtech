# -*- coding=UTF-8 -*-

import view

from flask import Flask

app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'

app.add_url_rule('/', view_func=view.Home.as_view('home'))
# app.add_url_rule('/view/user', view_func=view.User.as_view('user'))
# app.add_url_rule('/view/archieve',
#     view_func=view.Archieve.as_view('archieve'))
app.add_url_rule('/view/archieve_detail',
    view_func=view.ArchieveDetail.as_view('archieve_detail'))
# app.add_url_rule('/view/statistics',
#     view_func=view.Statistics.as_view('statistics'))
app.add_url_rule('/view/input_archieve_id',
    view_func=view.InputArchieveId.as_view('input_archieve_id'))
app.add_url_rule('/view/input_identity_card',
    view_func=view.InputIdentityCard.as_view('input_identity_card'))
app.add_url_rule('/view/archieve_list',
    view_func=view.ArchieveList.as_view('archieve_list'))


if __name__ == '__main__':
    app.run(port=5002)
