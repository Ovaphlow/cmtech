# -*- coding=UTF-8 -*-

import admin
import chaxun
import dangan
import globalvars
import index
import shangchuan
import test
import view
import yonghu

from flask import Flask


app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True
app.secret_key = 'Ovaphlow'
app.config['UPLOAD_FOLDER'] = globalvars.G_UPLOAD_PATH

app.add_url_rule('/',
    view_func=index.Index.as_view('index'))
app.add_url_rule('/test', view_func=test.Test.as_view('test'))
app.add_url_rule('/login', view_func=index.Login.as_view('login'))
app.add_url_rule('/logout', view_func=index.Logout.as_view('logout'))

app.add_url_rule('/chaxun', view_func=chaxun.ChaXun.as_view('chaxun'))
app.add_url_rule('/chakan/<rec_id>', view_func=dangan.ChaKan.as_view('chakan'))
app.add_url_rule('/daoru', view_func=shangchuan.DaoRu.as_view('daoru'))
app.add_url_rule('/luru', view_func=shangchuan.LuRu.as_view('luru'))
app.add_url_rule('/saomiao/<uid>',
    view_func=shangchuan.SaoMiao.as_view('saomiao'))
app.add_url_rule('/shangchuan/<rec_id>',
    view_func=shangchuan.ShangChuan.as_view('shangchuan'))
app.add_url_rule('/dangan/<rec_id>', view_func=dangan.DangAn.as_view('dangan'))
app.add_url_rule('/_upload_image_file',
    view_func=dangan.UploadImageFile.as_view('ulpic'))
app.add_url_rule('/xgmm', view_func=yonghu.XiuGaiMiMa.as_view('xgmm'))
app.add_url_rule('/delete_archieve/<archieve_id>',
    view_func=dangan.DeleteArchieve.as_view('delete_archieve'))
app.add_url_rule('/gen_code/<archieve_id>',
    view_func=dangan.GenCode.as_view('gen_code'))
app.add_url_rule('/dayin/<archieve_id>',
    view_func=dangan.DaYin.as_view('da_yin'))
app.add_url_rule('/exp2client/<rec_id>',
    view_func=dangan.Exp2Client.as_view('exp2client'))
app.add_url_rule('/dl_zip/<archieve_id>',
    view_func=dangan.DownloadZip.as_view('dl_zip'))

# 查询统计
app.add_url_rule('/chaxun/tsgz',
    view_func=chaxun.TeShuGongZhong.as_view('tsgz'))
app.add_url_rule('/chaxun/nglgw',
    view_func=chaxun.NvGuanLiGangWei.as_view('nglgw'))
app.add_url_rule('/chaxun/dytx', view_func=chaxun.DangYueTuiXiu.as_view('dytx'))
app.add_url_rule('/tongji',
    view_func=chaxun.TongJi.as_view('tong_ji'))
app.add_url_rule('/tongji_month',
    view_func=chaxun.TongjiMonth.as_view('tongji_month'))
app.add_url_rule('/tongji_time_slot',
    view_func=chaxun.TongjiTimeSlot.as_view('tongji_time_slot'))
app.add_url_rule('/tongji_archieve_log',
    view_func=chaxun.ArchieveLog.as_view('tongji_archieve_log'))
app.add_url_rule('/invoke_month',
    view_func=chaxun.InvokeMonth.as_view('invoke_month'))
app.add_url_rule('/invoke_time_slot',
    view_func=chaxun.InvokeTimeSlot.as_view('invoke_time_slot'))
app.add_url_rule('/invoke_log',
    view_func=chaxun.InvokeLog.as_view('invoke_log'))

# 管理员账号部分
app.add_url_rule('/admin', view_func=admin.Home.as_view('admin'))
app.add_url_rule('/admin/user_list',
    view_func=admin.UserList.as_view('admin user list'))
app.add_url_rule('/admin/user', view_func=admin.User.as_view('admin user'))
app.add_url_rule('/admin/add_user',
    view_func=admin.AddUser.as_view('admin add user'))
app.add_url_rule('/admin/archieve',
    view_func=admin.Archieve.as_view('admin archieve'))
app.add_url_rule('/admin/delete_archieve',
    view_func=admin.DeleteArchieve.as_view('admin delete archieve'))

# 浏览账号部分
app.add_url_rule('/view', view_func=view.Home.as_view('view_home'))
app.add_url_rule('/view/user', view_func=view.User.as_view('view_user'))
app.add_url_rule('/view/archieve',
    view_func=view.Archieve.as_view('view_archieve'))
app.add_url_rule('/view/archieve_detail',
    view_func=view.ArchieveDetail.as_view('view_archieve_detail'))
app.add_url_rule('/view/statistics',
    view_func=view.Statistics.as_view('view_statistics'))
app.add_url_rule('/view/input_archieve_id',
    view_func=view.InputArchieveId.as_view('view.input_archieve_id'))
app.add_url_rule('/view/input_identity_card',
    view_func=view.InputIdentityCard.as_view('view.input_identity_card'))
app.add_url_rule('/view/archieve_list',
    view_func=view.ArchieveList.as_view('view.archieve_list'))

if __name__ == '__main__':
    app.run()
