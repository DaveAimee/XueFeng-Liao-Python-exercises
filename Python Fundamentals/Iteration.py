# from collections import Iterable
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
#
# for value in d.values():
#     print(value)
#
# print(isinstance('abc', Iterable))
#
# print(isinstance(d, Iterable))
#
# L = ['A', 'B', 'C']
# for i, value in enumerate(L):
#     print(i, value)
#
# for x, y in [(1, 2), (3, 4)]:
#     print(x, y)

def findMinAndMax(L):
    if len(L)==0:
        return None, None
    min_value = L[0]
    max_value = L[0]
    for value in L:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    return min_value, max_value


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')











