# -*- coding: UTF-8 -*-
#参考文章 http://www.runoob.com/python3/python3-mysql.html
import pymysql
import module.config
class Mysqlclass:
	def __init__(self):
		self.db = pymysql.connect(module.config.MYSQL_HOST, module.config.MYSQL_USER, module.config.MYSQL_PWD, module.config.MYSQL_DB)

	def connMysql(self):
		cursor = self.db.cursor()
		return cursor

	def getOnedata(self, sql, param):
		cursor = self.db.cursor()
		cursor.execute(sql,param)
		result = cursor.fetchone()
		return result

	def __del__(self):
		self.db.close()