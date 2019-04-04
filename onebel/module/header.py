# -*- coding: UTF-8 -*-
#权限控制
from flask import Flask, url_for, request, make_response, session

class doHeader:
	def islogin(self):
		if session.get('isLogin'):
			return None
		else:
			return True
