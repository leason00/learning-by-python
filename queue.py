#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2018/2/27 15:32
"""


class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, item):
        self.list.insert(0, item)

    def dequeue(self):
        if self.list:
            return self.list.pop()
        return None

    def isEmpty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)


def hotPotato(namelist, num):
    """
    烫手山芋问题
    :param namelist:
    :param num: 传递次数
    :return:
    """
    queue = Queue()
    for name in namelist:
        queue.enqueue(name)

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()


if __name__ == "__main__":
    queue = Queue()
    print(queue.isEmpty())
    [queue.enqueue(i) for i in range(10)]
    print(queue.isEmpty())
    print(queue.list)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.size())
    print(queue.list)

    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))