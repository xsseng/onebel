# -*- coding: UTF-8 -*-
#权限控制
from flask import Flask, url_for, redirect, render_template, request, make_response, session
from module.riskManage import *
from module.Mysql import *
from module.header import *
from datetime import datetime,timedelta
import os

class doHeader:
	def islogin(self):
		if session.get('isLogin'):
			return None
		else:
			return True
