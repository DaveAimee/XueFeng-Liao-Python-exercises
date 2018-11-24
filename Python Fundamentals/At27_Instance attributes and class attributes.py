# 给实例绑定属性的方法是通过实例变量或者通过self变量。.
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 类属性
class Student(object):
    name = 'Student'