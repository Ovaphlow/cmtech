# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector
from flask import request

def get():
  template = globalvars.jinja_env.get_template('template/luru.html')
  return template.render()

def post():
  print 'DangAnHao:', request.form['aid']
  print 'ShenFenZheng:', request.form['idcard']
  print 'XingMing:', request.form['name']
  print 'XingBie:', request.form['gender']
  print 'ChuShengRiQi:', request.form['dob']
  print 'YuTuiXiuRiQi:', request.form['retiredate']
  print 'NvGuanLiGangWei:', request.form.getlist('check')
  if 'female' in request.form.getlist('check'):
    print 'female'
  if 'stow' in request.form.getlist('check'):
    print 'stow'
  #print 'TeShuGongZhong:', request.form.getlist('stow')
  template = globalvars.jinja_env.get_template('template/luru.html')
  return template.render()
