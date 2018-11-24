import types
# 使用type()
print(type(123))
print(type('str'))

  # 判断是否为函数
def fn():
    pass


print(type(fn)==types.FunctionType)

# 使用isinstance()
isinstance(Peter,Person)

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，
# 比如，获得一个str对象的所有属性和方法