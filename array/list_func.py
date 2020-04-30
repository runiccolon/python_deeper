# -*- coding:utf-8 -*-
"""
列表操作
"""

l = [1, 2, 3, 4, 5, 4]
print(l.__contains__(1))    # 列表l是否包含元素1

print(l.count(4))

# l.__delitem__(0)    # 把位于0的元素删除
# l.remove(4)     # 删除l中第一次出现的4

print(l.index(4))  # 在l中找到元素4第一次出现的位置

print(l.__iter__())   # 获取l的迭代器

print(l.__mul__(2))     # l * 2
# print(l.__imul__(2))        # l *= 2    就地重复拼接,l变化
print(l.__rmul__(2))    # 2 * l


