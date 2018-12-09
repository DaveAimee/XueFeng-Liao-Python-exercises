# List. list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = [3, 'Bob', 'Tracy']
len(classmates)
# 按照下标取出list中的元素
print(classmates[0]+3)
print(classmates[1])
print(classmates[2])

# 对List的相关操作
classmates.append('Adam')
classmates.insert(1,'Jack')
classmates.pop()  # 删除List末尾的元素
classmates.pop(1)  # 删除指定位置的元素
# 倒序获取元素
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# Tuple。 tuple和list非常类似，但是tuple一旦初始化就不能修改。
classmates = ('Michael', 'Bob', 'Tracy')
t = (1, 2)
blank_tuple = ()
one_element = (1,)  # 定义只有一个元素的tuple

# Excercise

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
