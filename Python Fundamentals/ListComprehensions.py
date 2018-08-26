# import os
# m = list(range(1, 11))
# print(m)
#
# print([x*x for x in m])
#
# print([m + n for m in 'ABC' for n in 'YZ'])
#
#
# print([d for d in os.listdir('.')])
#
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
#
# for k, v in d.items():
#     print(k + '=' + v)

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if (isinstance(s,str))]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')