# -*- coding: UTF-8 -*-
from . import users
from flask import request, render_template, session, redirect, url_for, make_response
from module.Mysql import *
from module.loginAuth import *

@users.route('/index')
def index():
	return render_template('index.html')

@users.route('/login', methods = ['GET', 'POST',])
def login():
    if request.method == 'GET':
        return render_template('login.html',name=None)
    else:
        username = request.form['username']
        password = request.form['password']
        t = Mysqlclass()
        q = t.getOnedata("SELECT * from crm_user where username = %s and password = %s",(username,password))
        if q:
            session.permanent = True
            session['isLogin'] = 1
            session['username'] = username
            return redirect(url_for('admin.member'))
        else:
            return 'password error'
        #处理登录逻辑

@users.route('/member', methods=["GET",])
@user_login_status_check
def member():
	return 'hello' + str(session.get('username'))