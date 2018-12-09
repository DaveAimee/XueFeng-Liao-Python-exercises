# 列表生成式:
# 以公式生成list
print([x * x for x in range(1, 11)])

print([m + n for m in 'ABC' for n in 'XYZ'])

dict = {'1': 3, '2': 6}
t = ((name,value) for name,value in dict.items() if  name == '1')
print(t)

