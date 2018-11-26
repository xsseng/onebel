from flask import Flask, url_for, redirect
from flask import render_template
from flask import request
from flask import make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

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

    return response


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)
