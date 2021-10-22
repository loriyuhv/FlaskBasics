"""
内容回顾：
1. 装饰器
问题：什么是装饰器？

问题：手写装饰器
问题：装饰器都在哪里用过？
"""

# 1. 为什么要用装饰器
"""
在不改变原函数的基础上，对函数执行前后进行自定义操作。
"""
import functools


def swapper(func):
    @functools.wraps(func)      # 作用：将原函数的 元信息 赋值给现有的函数
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner


"""
1. 执行swapper函数，并将被装饰的函数当做参数。swapper(index)
2. 将第一步的返回值，重新赋值给新index = swapper(老index)
"""


@swapper
def index(a1):
    return a1 + 1000
# 等价于
# index = swapper(index)


v = index(500)
print(v)
print(index.__name__)   # 输出 inner

# # 执行
# v = index(500)
# print(v)
#
# print(index.__name__)   # 取函数名
