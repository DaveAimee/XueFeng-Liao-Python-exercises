# import itertools
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))
#
# cs = itertools.cycle('ABC')
# print(cs)
# # for c in cs:
# #     print(c)
#
# # chain()
# # for c  in itertools.chain(cs, natuals):
# #     print(c)
#
# # groupby()
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))
from functools import reduce


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    g = ((2 * x + 1) for x in range(N))
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    nl = list(g)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    for i in range(N):
        if i % 2 == 1:
            nl[i] = -nl[i]
    nl = list(map(lambda x:  4 / x, nl))

    # step 4: 求和:
    return reduce(lambda x, y: x + y, nl)

print(pi(10))