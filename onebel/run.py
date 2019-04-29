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

from views import *

app.register_blueprint(users)
app.register_blueprint(api)
	
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)
