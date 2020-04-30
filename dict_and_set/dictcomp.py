# -*- coding:utf-8 -*-
"""
字典推导
"""

# 创建字典的方式
a = dict(one=1, two=2, three=3)
b = {"one": 1, "two": 2, "three": 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({"one": 1, "two": 2, "three": 3})
if a == b == c == d == e:
    print('y')


# 字典推导
name_age_list = [('Zoe', 10000), ('Zed', 35), ('Lux', 23), ('Ezra', 26)]
name_age = {name: age for name, age in name_age_list}
print(name_age)

name_age_upper = {name.upper(): age for name, age in name_age.items() if age < 100}
print(name_age_upper)
