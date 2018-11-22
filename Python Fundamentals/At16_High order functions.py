from functools import reduce
# 变量可以指向函数
f = abs
print(f(-10))

# 函数名也是变量
# abs = 10


# 函数名作为参数
def add(x, y, f):
    return f(x) + f(y)


# map()和reduce()函数

# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  # 结果是一个Iterator
list(r)


def add(x, y):
    return x + y

reduce(add, [1, 3, 5, 7, 9])


# filter()函数: filter()函数把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False来决定保留还是丢弃。
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

# 排序算法
sorted([36, 5, -12, 9, -21], key= abs)
