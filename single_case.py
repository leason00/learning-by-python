#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2018/3/1 15:58
"""


# 单例模式
class Single(object):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Single, cls).__new__(cls)
        return cls._instance


obj1 = Single()
obj2 = Single()

obj1.attr1 = 'value1'
print(obj1.attr1, obj2.attr1)

print(obj1 is obj2)


# 共享属性
class Borg(object):
    _state = {}
    def __new__(cls):
        ob = super(Borg, cls).__new__(cls)
        ob.__dict__ = cls._state
        return ob

