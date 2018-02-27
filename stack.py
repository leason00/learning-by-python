#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2018/2/27 14:16
"""


class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.list:
            return self.list.pop()
        return None

    def peek(self):
        if self.list:
            return self.list[-1]
        return None

    def size(self):
        return len(self.list)


def par_check(string):
    """
    符号匹配 如：{{([][])}()}}
    :param string:
    :return:
    """
    s = Stack()
    state = True
    index = 0
    swtich = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

    while index < len(string) and state:
        if string[index] in "{([":
            s.push(string[index])
        else:
            if s.isEmpty():
                state = False
            else:
                if swtich[s.pop()] != string[index]:
                    state = False

        index = index + 1

    if state and s.isEmpty():
        return True
    else:
        return False




if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())
    [stack.push(i) for i in range(10)]
    print(stack.list)
    print(stack.isEmpty())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())


    print(par_check("{{([][])}()}}"))


