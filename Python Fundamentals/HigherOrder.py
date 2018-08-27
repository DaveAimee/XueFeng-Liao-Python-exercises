# from functools import reduce
# x = abs(-10)
# print(x)
#
#
# def add(x, y, f):
#     return f(x) + f(y)
#
#
# print(add(-1, 2, abs))
#
#
# def f(x, y):
#     return x+y
#
#
# # r = map(f, [1,2,3,4,5,6])
#
#
# #print(list(r))
#
#
# print(reduce(f, [1, 2, 3, 4, 5]))
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# def chartonum(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
#
# print(reduce(fn, map(chartonum, '13579')))
#
# from functools import reduce
#
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
# def strtoint(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def chartonum(s):
#         return DIGITS[s]
#     return reduce(fn, map(chartonum, s))
from functools import reduce
# Excercise 1
# 测试:


def normalize(name):
    return name[0].upper()+name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# Excercise 2
# 测试：

def prod(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# Excercise 3
# 测试

def str2float(s):
    s = s.split('.')
    if len(s) == 1:
        return reduce(lambda x, y: x*10+y, map(int, s[0]))
    else:
        return reduce(lambda x, y: x*10+y, map(int, s[0]+s[1]))/pow(10, len(s[1]))


print(str2float('321'))


print(str2float('1.521'))

print(str2float('1.0'))









