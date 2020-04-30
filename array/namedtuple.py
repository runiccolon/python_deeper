# -*- coding:utf-8 -*-
"""
具名元组
"""
from collections import namedtuple

Leaner = namedtuple('Leaner', 'name sex age subject')    # 创建一个名为Leaner的类
zhao = Leaner('乾', '男', 25, ('Language', 'Python'))
print(zhao)
print(zhao.name)

# 具名元组的属性和方法
print(Leaner._fields)
Zoe = namedtuple('Zoe', 'lover foe')
hero_data = ('佐伊', '女', 21000, Zoe('Ezreal', 'Lux'))
hero = Leaner._make(hero_data)
ordered_dict = hero._asdict()
print(ordered_dict)
for key, value in ordered_dict.items():
    print(key + ':', value)