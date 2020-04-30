# -*- coding:utf-8 -*-
"""
切片
"""

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
l[2:5] = [100]
print(l)

from random import random
for i in (random() for i in range(10**7)):
    print(i)
