# coding:utf-8

from functools import wraps


def decorator_name(f):
    @wraps(f)   # @wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    return ("Function is running")


# can_run = True
# print(func())
# # Output: Function is running

can_run = False
print(func())
# Output: Function will not run