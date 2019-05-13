# -*- coding: UTF-8 -*-
from . import api
from flask import request, render_template, redirect, url_for, make_response
from module.riskManage import *
from module.Mysql import *
from module.public import *

@api.route('/test/')
@api.route('/test/<name>')
def hello(name=None):
    return render_template('test.html',name=name)

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

@api.route('/getdata/<onebelkey>', methods = ['GET', 'POST', 'OPTIONS'])
def get_data(onebelkey):
    if request.method == 'POST':
        onebelkey = request.form['onebelkey']
        where_field = request.form['where_field']
        where_value = request.form['where_value']
        #查询onebel key是否配置
        t = Mysqlclass()
        odresult = t.getOnedata("SELECT * from onebel_data where key_name = %s",(onebelkey))
        if not odresult:
            return 'onebelkey 不存在'
        else:
            dbname = odresult[2]
            tbname = odresult[3]
            keyvalues = odresult[4]
        #查询是否存在恶意SQL注入
        if api_sqli_waf(where_value) is False:
            return '试图攻击系统被拦截'
        #查询数据
        sql = 'SELECT {keyvalues} from {dbname}.{tbname} where {field} = "{value}"'.format(keyvalues=keyvalues, dbname=dbname, tbname=tbname, field=where_field, value=where_value)
        query_data = t.getOnedata(sql,None)
        if query_data:
            result = query_data[0]+str(sql)
        else:
            result = 'no data'

        #查询是否配置风控规则，无规则直接返回数据
        isRiskrule = t.getOnedata("SELECT * from risk_rule where key_name = %s and status = 1",(onebelkey))
        if not isRiskrule:
            return result
        else:
            #获取风控规则配置数据
            rule_name = isRiskrule[1]
            risk_type = isRiskrule[2]
            rule_config = isRiskrule[3]
            key_name = isRiskrule[4]
            status = isRiskrule[5]
            #这里开始写的代码可以进行二次开发，原生态办法基于ip做风控，这里可以改写为用户行为或者其他设备指纹风控策略
            #以IP为例子
            #获取设备指纹
            ip = request.remote_addr
            user_agent = request.user_agent
            exec(rule_config)
            r = Rmbyip()
            riskScore = r.iprm(ip, 50, where_value, 50)

            #实例化风控类

            return rule_config











