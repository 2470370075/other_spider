import redis
#
# r=redis.Redis(host='192.168.241.134', port=6379)
# r.set('x1','1')
# v=r.get('x1')
# # r.delete('links_seen')
# # r.delete('links_queue')
# print(v)
# print(r.keys())
# print(r.type('x1'))
# print(r.type('links_seen'))
# a=r.smembers('links_seen')
# print(a)
# print(r.lrange('links_queue',0,10))
# r.rpush('queue','1')
# r.lpop('queue')
# r.lpop('queue')

# s="<td>\r\n<p>排名</p>\r\n</td>': '<td>\r\n<p>98</p>\r\n</td>"
# ss="".join(s)
# print(ss)
# print(type(ss))


# dic = {'a':1,'b':2,'c':3}
# for k,v in dic.items():
#     print(k,v)
# print(dic.items())
# print(*dic.items())                             # *脱衣服  zip解压，往下拉拉链
# k,v = zip(*dic.items())
# print(k,v)
#
# def f():
#     c=(['a','b'],['c','d'])
#     return c


dic = {'x1':'1','x2':2}
print(dic['x3'])