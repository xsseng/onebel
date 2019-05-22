# -*- coding: UTF-8 -*-
from . import api
from flask import request, render_template, redirect, url_for, make_response, jsonify
from module.riskManage import *
from module.Mysql import *
from module.public import *
import time

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
    r = Rmpublic()
    if request.method == 'POST':
        onebelkey = request.form['onebelkey']
        where_field = request.form['where_field']
        where_value = request.form['where_value']

        #查询onebel key是否配置
        t = Mysqlclass()
        odresult = t.getOnedata("SELECT * from onebel_data where key_name = %s",(onebelkey))
        if not odresult:
            log = '404, onebekey is not found,onebelkey is' + str(onebelkey)
            data = {'code': '404', 'onebel_data': None, 'riskrulelog':log}
            r.setkey(onebelkey+where_field+where_value,str(data))
            return jsonify(data)
        else:
            dbname = odresult[2]
            tbname = odresult[3]
            keyvalues = odresult[4]

        #此处不可以预编译，需要防止SQL注入的出现
        if api_sqli_waf(where_value) is False:
            log = 'is a attack. ip is '+str(request.remote_addr)
            data = {'code': '911', 'onebel_data': None, 'riskrulelog':log}
            r.setkey(onebelkey+where_field+where_value,str(data))
            return jsonify(data)

        #执行SQL语句查询数据
        sql = 'SELECT {keyvalues} from {dbname}.{tbname} where {field} = "{value}"'.format(keyvalues=keyvalues, dbname=dbname, tbname=tbname, field=where_field, value=where_value)
        query_data = t.getOnedata(sql,None)
        if query_data:
            result = query_data[0]
        else:
            log = 'no select from database onebeldata by keys'
            data = {'code': '500', 'onebel_data': None, 'riskrulelog':log}
            r.setkey(onebelkey+where_field+where_value,str(data))
            return jsonify(data)

        #查询是否配置风控规则，无规则直接返回数据，有规则则获取风控规则配置后计算风控评分比对后在决定是否返回数据
        isRiskrule = t.getOnedata("SELECT * from risk_rule where key_name = %s and status = 1",(onebelkey))
        if not isRiskrule:
            log = 'no risk rule'
            data = {'code': '200', 'onebel_data':result, 'riskrulelog':log}
            r.setkey(onebelkey+where_field+where_value,str(data))
            return jsonify(data)
        else:
            rule_name = isRiskrule[1]
            risk_type = isRiskrule[2]
            rule_config = isRiskrule[3]
            key_name = isRiskrule[4]
            status = isRiskrule[5]
            rmtype = r.gettype(rule_config)
            '''
            这里开始开始进行二次开发
            rmtype为在后台配置的设备指纹字段，诸如ip、 mac、 mime
            风控计算写在riskManage.py里
            输出结果为riskScore，根据riskScore决定是否缓存数据到redis供服务器读取
            '''
            if rmtype == 'maxip':
                ip = request.remote_addr
                maxip = r.getconfig(rule_config)
                rip = Rmbyip()
                riskScore = rip.iprm(ip, maxip, where_value)
                #
            elif rmtype == 'maxage':
                user_agent = request.user_agent
                riskScore = 'maxage'

            #对比评分
            niceScore = r.getniceScore()
            if int(riskScore) >= int(niceScore):
                log = "getdata success,its securty request.---niceScore:" + str(niceScore) + "---riskScore:" + str(riskScore)
                data = {"code": "200", "onebel_data": result, "riskrulelog":log}
                r.setkey(onebelkey+where_field+where_value,str(data))
            else:
                #风控评分不通过，这里需要记录风险事件
                log = "getdata error,because didt pass rule.---niceScore:" + str(niceScore) + "---riskScore:" + str(riskScore)
                data = {"code": "200", "onebel_data": None, "riskrulelog":log}
                setdata = '{"code": "200", "onebel_data": None, "riskrulelog":"'+str(log)+'"}'
                r.setkey(onebelkey+where_field+where_value,str(setdata))
                #记录风险事件
                risk_time = time.asctime(time.localtime(time.time()))
                t.insertdata("INSERT INTO risk_count (rule_name, risk_type, time , detail) VALUES (%s,%s,%s,%s)",(rule_name, risk_type, risk_time, onebelkey+where_field+where_value+str(data)))
            return jsonify(data)

@api.route('/server/getdata', methods = ['GET',])
def sget_data():
    keyhash = request.args.get('keyhash')
    r = Redisclass()
    rob = r.redisCon()
    result = rob.get(keyhash)
    return jsonify(result)








