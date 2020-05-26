"""
    支持函数式编程的包
"""

from functools import reduce
from operator import mul


def fact(n):
    """
    使用reduce和一个匿名函数计算阶乘
    :param n:
    :return:
    """
    return reduce(lambda a, b: a * b, range(1, n + 1))


def fact1(n):
    return reduce(mul, range(1, n+1))

