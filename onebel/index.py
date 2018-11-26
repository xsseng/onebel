from flask import Flask, url_for, redirect, render_template, request, make_response
from module.riskManage import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Onebel is workerd'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html',name=name)

@app.route('/api/data/<onebelkey>', methods = ['POST', 'OPTIONS'])
def onebel_data(onebelkey):
    if request.method == 'POST':
        onebel = request.form['username']
        response = make_response(onebelkey + '=' + onebel)
        response.headers['Access-Control-Allow-Origin'] = '*'
        username = request.form.get('username')
        #风险控制信息
        ip = request.remote_addr
        user_agent = request.user_agent

        #类文件
        t = Helloclass()
        t.testhello('x')
        print(ip, user_agent)

    return response


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)
