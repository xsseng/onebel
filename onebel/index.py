from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html',name=name)

@app.route('/api/data/<onebelkey>', methods=['POST','GET'])
def onebel_data(onebelkey):
    return onebelkey + '=' + request.args.get('data', '')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)