# -*- coding:utf-8 -*-
"""
memoryview不是用于创建或存储字节序列的,而是共享内存,eg:PIL库
"""
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)