# -*- coding: UTF-8 -*-
#参考博客 https://www.cnblogs.com/melonjiang/p/5342505.html
#风控系统只输出风控测评分，不做任何其他操作
#维度： IP  User_agent 
import redis
import module.config
class Helloclass:
	def testhello(self, ip, user_agent, onebelkey):
		print("it's worked")
		print("useragent:" + str(user_agent))
		#-*-    记录数据     -*-#

		r = Redisclass.redisCon(self)
		r.set(onebelkey, ip, ex=36000)#存入onekey与访问IP
		Redisclass.setIPrisk(r, ip)#设置Ip访问自增，这里没有过期时间，需要走一遍逻辑

		print(r.get(ip))
		print(r.get(onebelkey))

		#-*-    计算得分    -*-#
		if int(r.get(ip)) >= 10:
			riskScore = 0
		elif int(r.get(ip)) >= 10/2:
			riskScore = 100 * 0.5 * 0.3 #100总分 * 打折系数 * 权重比
		else:
			riskScore = 100 * 0.3

		print('riskScore = ' , riskScore)



class Redisclass:
	def redisCon(self):
		#flask https://blog.csdn.net/zhengwantong/article/details/79497699
		#创建连接池
		pool = redis.ConnectionPool(host=module.config.DB_HOST,port=module.config.DB_PORT,db=module.config.DB,decode_responses=True,password=module.config.DB_PWD)
		#链接对象
		r = redis.Redis(connection_pool=pool)
		return r

	def setIPrisk(r, ip):
		r.incr(ip, 1)
		req_num = r.get(ip)
		r.set(ip, req_num, ex=36000)
		#ip的写法incr(self, name, amount=1) 不存在则创建，存在则自增，在此之后增加缓存时间
		#https://github.com/stefanlei/notes/blob/55ff97a4c040ccc2f74b82fe5a067bdf856f83e4/Redis/8.%20Python%20操作%20redis.md

