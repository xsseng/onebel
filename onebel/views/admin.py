# -*- coding: UTF-8 -*-
from . import users
from flask import request, render_template, session, redirect, url_for, make_response
from module.Mysql import *
from module.public import *

@users.route('/index')
def index():
	return 'onebel is worked!'

@users.route('/login', methods = ['GET', 'POST',])
def login():
    if request.method == 'GET':
        if session.get("isLogin", "1"):
            return redirect(url_for('admin.member'))
        else:
            return render_template('login.html')           
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

@users.route('/logout', methods = ['GET',])
def logout():
        session.permanent = True
        session['isLogin'] = 0
        return 'logout success'

@users.route('/member', methods=["GET",])
@user_login_status_check
def member():
	return render_template('index.html')

@users.route('/editpwd', methods = ['GET', 'POST',])
@user_login_status_check
def editpwd():
    if request.method == 'GET':
        return render_template('edit-password.html')
    else:
        username = get_user()
        t = Mysqlclass()
        q = t.updatedata("UPDATE crm_user SET password = %s WHERE username = %s and password = %s",(request.form['newpwd'],username,request.form['oldpwd']))
        return q









