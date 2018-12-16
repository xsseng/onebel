# -*- coding: UTF-8 -*-
#参考博客 https://www.cnblogs.com/melonjiang/p/5342505.html
#风控系统只输出风控测评分，不做任何其他操作
#维度： IP  User_agent 
import redis
class Helloclass:
	def testhello(self, ip, user_agent):
		print("it's worked")
		print("ip:" + ip)
		print("useragent:" + str(user_agent))
		#flask https://blog.csdn.net/zhengwantong/article/details/79497699
		#创建连接池
		pool = redis.ConnectionPool(host='www.inetsrc.com',port=6379,decode_responses=True)
		#链接对象
		r = redis.Redis(connection_pool=pool)


		#ip的写法incr(self, name, amount=1) 不存在则创建，存在则自增，在此之后增加缓存时间


