
#
# # def log(func):
# #     def wrapper(* args, ** kw):
# #         print('call %s ()' % func.__name__)
# #         return func(* args, ** kw)
# #     return wrapper
#
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
#
# @ log('excecute')
# def now():
#     print('2005-5-12')
#
#
# now()

import time, functools


def metric(fn):
    functools.wraps(fn)

    def wrapper(* args, ** kw):
        start = time.clock()
        res = fn(*args, ** kw)
        elapsed = (time.clock() - start)
        print('%s executed in %s ms' % (fn.__name__, elapsed * 1000))
        return res
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')









