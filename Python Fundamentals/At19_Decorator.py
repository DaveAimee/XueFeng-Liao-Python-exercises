import functools
# 装饰器
# 在代码运行期间动态增加功能的方式
# 本质上，decorator就是一个返回函数的高阶函数。
# 所以，我们要定义一个能打印日志的decorator，可以定义如下：
# 实现日志功能:
def log(func):  #  装饰器接受一个函数作为参数
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():  # 相当于执行了语句 now = log(now)
    print('2015-3-25')



# decorator本身需要传入参数的情况
def log1(text):  # 效果等于 now = log('execute')(now)
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


now()


@log1('execute')
def now1():  # 相当于执行了语句 now = log(now)
    print('2015-3-25')


now1()