# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#
# print([L[0], L[1], L[2]])
#
# print(L[0:3])
#
# print(L[:3])
#
# print(L[-2:])


# 去掉字符串首尾的空格
def trim(str):
    start = 0
    end = len(str)
    while start < end:
        if str[start] == ' ':
            start += 1
        if str[end-1] == ' ':
            end -= 1
        if str[start] != ' ' and str[end-1] != ' ':
            break

    return str[start:end]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
