# 字典: dict
# 例如：
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 取用或修改： d['Michael'] = 67
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
# >>> 'Thomas' in d
# False
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
#
# >>> d.get('Thomas')
# >>> d.get('Thomas', -1)
# -1
# 删除一个key，用pop(key)方法，对应的value也会从dict中删除.


# 集合: set
# 初始化:
s = set([1, 2, 3])
s.add(9)
s.remove(3)
# 两个集合可以做数学意义上的交集和并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2

