# Generator: 如果列表元素可以按照某种算法推算出来，
#            在循环的过程中不断推算出后续的元素.

L = [x * x for x in range(10)]  # 生成式
print(L)

g = (x * x for x in range(10))  # 生成器

for n in g:
    print(n)

# 函数生成器。生成斐波那契数列


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'



