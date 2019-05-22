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

	def execSql(self, sql):
		cursor = self.db.cursor()
		result = cursor.execute(sql)
		return result

	def getOnedata(self, sql, param):
		cursor = self.db.cursor()
		cursor.execute(sql,param)
		result = cursor.fetchone()
		return result

	def getAlldata(self, sql, param):
		cursor = self.db.cursor()
		cursor.execute(sql,param)
		result = cursor.fetchall()
		return result

	def updatedata(self, sql, param):
		cursor = self.db.cursor()
		try:
			cursor.execute(sql,param)
			self.db.commit()
			return 'update ok'
		except:
			return 'mysql error'

	def insertdata(self, sql, param):
		cursor = self.db.cursor()
		try:
			cursor.execute(sql,param)
			self.db.commit()
			return 'exec success'
		except:
			return 'mysql error'

	def issetdata(self, sql, param):
		cursor = self.db.cursor()
		cursor.execute(sql,param)
		result = cursor.fetchone()
		if(result):
			return 'data is isset'
		else:
			return 'data is null'

	def __del__(self):
		self.db.close()



