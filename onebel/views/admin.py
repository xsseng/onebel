# -*- coding: UTF-8 -*-
from . import main
from flask import request, render_template, session, redirect, url_for, make_response
from module.Mysql import *
from module.loginAuth import *

@main.route('/index')
def index():
	return 'hello world!'

@main.route('/login', methods = ['GET', 'POST'])
def login(name=None):
    if request.method == 'GET':
        return render_template('login.html',name=name)
    else:
        username = request.form['username']
        password = request.form['password']
        t = Mysqlclass()
        q = t.getOnedata("SELECT * from crm_user where username = %s and password = %s",(username,password))
        if q:
            session.permanent = True
            session['isLogin'] = 1
            session['username'] = username
            return redirect('/admin/member')
        else:
            return 'password error'
        #处理登录逻辑

@main.route('/member')
@loginAuth
def member(name=None):
	return 'hello' + str(session.get('username'))