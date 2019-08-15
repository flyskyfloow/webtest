# coding=utf8
class MyTest(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def __str__(self):
        # print("str test" + self.name + "*****" + self.sex)
        return '%s   +++++   %s' % (self.name, self.sex)

    def __set_name__(self, owner, name):
        pass

    def say(self):
        print("hello say")


class Person(MyTest):
    def __init__(self,path):
        self.path = path

    def see(self):
        print(self.path)


