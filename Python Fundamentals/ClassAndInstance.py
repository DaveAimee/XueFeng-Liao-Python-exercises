# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#
# bart = Student('Bart', 3)
#
# bart.print_score()
#
# bart.__name = 'test'
#
# bart.print_score()


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender != 'male' and gender != 'female':
            raise ValueError('性别不正确')
        else:
            self.__gender = gender


bart = Student('Q', 'male')


print(type(bart))






