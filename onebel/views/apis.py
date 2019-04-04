# -*- coding: UTF-8 -*-
from . import api
from flask import request, render_template, redirect, url_for, make_response
from module.riskManage import *

@api.route('/test/')
@api.route('/test/<name>')
def hello(name=None):
    return render_template('index.html',name=name)

@api.route('/data/<onebelkey>', methods = ['POST', 'OPTIONS'])
def onebel_data(onebelkey):
    if request.method == 'POST':
        #开始取值
        onebelkey = request.form['username']
        #风险控制信息
        ip = request.remote_addr
        user_agent = request.user_agent

        #类文件
        #风控计算
        t = Helloclass()
        riskScore = t.testhello(ip, user_agent, onebelkey)

        #输出
        response = make_response(onebelkey + '=' + onebelkey)
        response.headers['Access-Control-Allow-Origin'] = '*'

    return response