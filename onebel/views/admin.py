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
        q = t.getOnedata("SELECT * from onebel_user where username = %s and password = %s",(username,password))
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
        q = t.updatedata("UPDATE onebel_user SET password = %s WHERE username = %s and password = %s",(request.form['newpwd'],username,request.form['oldpwd']))
        return q

@users.route('/adduser', methods = ['GET', 'POST',])
@user_login_status_check
def adduser():
    if request.method == 'GET':
        return render_template('add-user.html')
    else:
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        if len(username) ==0 or len(password) == 0:
            return '用户名和密码不能为空'
        t = Mysqlclass()
        if t.getOnedata("SELECT * from onebel_user where username = %s",(username)):
            return '用户名已经存在'
        else:
            q = t.insertdata("INSERT INTO onebel_user (username,password,privilege) VALUES (%s,%s,%s)",(username,password,'1'))
            return q
        #return str(q[0])

@users.route('/userlist', methods = ['GET',])
@user_login_status_check
def userlist():
    if request.method == 'GET':
        t = Mysqlclass()
        q = t.getAlldata("SELECT * from onebel_user",None)
        return render_template('user-list.html', userlist = q)
        #return str(q[0])

#风控管理
@users.route('/addriskrule', methods = ['GET','POST'])
@user_login_status_check
def addriskrule():
    if request.method == 'GET':
        return render_template('add-riskrule.html')
    else:
        return '还没写'

@users.route('/editriskrule', methods = ['GET',])
@user_login_status_check
def editriskrule():
    if request.method == 'GET':
        return render_template('edit-riskrule.html')
    else:
        return '还没写'

@users.route('/addapi', methods = ['GET',])
@user_login_status_check
def addapi():
    if request.method == 'GET':
        return render_template('add-alarmapi.html')
    else:
        return '还没写'

#数据管理
@users.route('/adddata', methods = ['GET','POST'])
@user_login_status_check
def adddata():
    if request.method == 'GET':
        return render_template('add-data.html')
    else:
        return '还没写'
        #return str(q[0])

@users.route('/editdata', methods = ['GET',])
@user_login_status_check
def editdata():
    if request.method == 'GET':
        return render_template('edit-data.html')
    else:
        return '还没写'






