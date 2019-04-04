# -*- coding: UTF-8 -*-
from flask import Flask
from datetime import datetime,timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days = 7)

@app.route('/')
def hello_world():
	return 'onebel is worked!'

from views import main as main
from views import api as api

app.register_blueprint(main)
app.register_blueprint(api)
	
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)
