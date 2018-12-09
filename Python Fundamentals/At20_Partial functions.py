import functools
# Python的functools模块提供了很多有用的功能，
# 其中一个就是偏函数（Partial function）。

print(int('10', base=8))
int8 = functools.partial(int, base=8)

print(int8('10'))
