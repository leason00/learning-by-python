#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2018/2/27 16:20
"""


class Deque:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)

    def add_front(self, item):
        self.list.append(item)

    def add_rear(self, item):
        self.list.insert(0, item)

    def remove_front(self):
        return self.list.pop()

    def remove_rear(self):
        return self.list.pop(0)


def palindrome(string):
    """
    判断是否回文
    :param string: 待判断字符串
    :return:
    """
    deque = Deque()
    state = True
    for i in string:
        deque.add_front(i)

    while deque.size() > 1 and state:
        top = deque.remove_front()
        end = deque.remove_rear()
        if top != end:
            state = False
    return state

if __name__ == "__main__":
    print(palindrome("123456654321"))
