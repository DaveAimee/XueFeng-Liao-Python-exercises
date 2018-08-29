# print(sorted([36, 5, -12, 9, -21]))
#
# def f(x):
#     return abs(x)
#
# print(sorted([36, 5, -12, 9, -21],key = abs))
#
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# excercise

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]

def by_score(t):
    return t[1]


L2 = sorted(L, key=by_name)
print(L2)


L2 = sorted(L, key=by_score)
print(L2)

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print(calc_sum(1, 2, 3))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())












