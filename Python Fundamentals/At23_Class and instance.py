# 定义类常用模板
class Student(object):
    pass

# 创建实例
bart = Student()
print(bart)

# 给一个实例变量绑定属性
bart.name = 'Bart Simpson'

# 由于类可以起到模板的作用，
# 因此，可以在创建实例的时候，
# 把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，
# 在创建实例的时候，就把name，score等属性绑上去：
class Student1(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

Lucas = Student1('Lucas',83)

# 数据封装
class Student2(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

Sabrina = Student2('Sabrina',83)
Sabrina.print_score()
