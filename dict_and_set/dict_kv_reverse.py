# coding:utf-8

dict1 = {
    (1, 2): 'first',
    (2, 3): 'first',
}

reverse_dict1 = dict([(value, key) for (key, value) in dict1.items()])
print(reverse_dict1)


# 判断两个自定义对象是否相等
class Trip():
    def __init__(self):
        pass

a = Trip()
b = a
c = Trip()
print(a == b)
print(a == c)
print(id(Trip()))

# 重写__hash__和__eq__方法来自定义对象相同判别方法

class Student(object):
    def __init__(self, name, age, sid):
        self.name = name
        self.age = age
        self.sid = sid

stu1 = Student("zhong", 15, 11198)
stu2 = Student("zhong", 15, 11198)

print(set([stu1, stu2]))
# 输出：{<__main__.Student object at 0x0030FE10>, <__main__.Student object at 0x0030FAD0>}
# set()判别结果为False

class Student1(object):
    def __init__(self, name, age, sid):
        self.name = name
        self.age = age
        self.sid = sid

    def __eq__(self, other):
        return self.name == other.name and \
               self.age == other.age and \
               self.sid == other.sid

    def __hash__(self):
        return hash((self.name, self.age, self.sid))

stu1 = Student1("zhong", 15, 11198)
stu2 = Student1("zhong", 15, 11198)
print(set([stu1, stu2]))

