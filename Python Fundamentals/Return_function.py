def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# print(calc_sum(1, 2, 3))
#
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
#
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f())



def createCounter():
    def __all_iter():
        n = 1
        while True:
            yield n
            n += 1
    it = __all_iter()

    def counter():
        return next(it)
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
