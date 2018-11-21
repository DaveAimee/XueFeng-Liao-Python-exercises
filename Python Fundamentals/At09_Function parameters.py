# 位置参数:
def power(x):
    return x*x

# 默认参数:
def power(x, n=2):
    s=1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 默认参数必须指向不变对象
# 错误示例:
#     def add_end(L=[]):
#     L.append('END')
#     return L
# 正确示例:
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# 可变参数:


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 在函数内部，参数numbers接收到的是一个tuple。
# 如果已经有一个list或者tuple,要调用一个可变参数的做法:


nums = [1, 2, 3]
calc(*nums)

# 关键字参数：


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Adam', 45, gender='M', job='Engineer')


# 命名关键字参数：
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 只接收city和job作为关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)

# 如果函数定义中已经有了一个可变参数，
# 后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)