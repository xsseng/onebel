from flask import Flask, url_for, redirect, render_template, request, make_response
from module.riskManage import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Onebel is workerd'

@app.route('/test/')
@app.route('/test/<name>')
def hello(name=None):
    return render_template('index.html',name=name)

@app.route('/login/')
def login(name=None):
    return render_template('login.html',name=name)


@app.route('/api/data/<onebelkey>', methods = ['POST', 'OPTIONS'])
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


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)
