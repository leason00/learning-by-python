#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2018/2/27 9:50
"""


class SortedDict(dict):
    def __init__(self):
        self.list = []
        super(SortedDict, self).__init__()

    def __setitem__(self, key, value):
        self.list.append(key)

        super(SortedDict, self).__setitem__(key, value)

    def __getitem__(self, key):
        if key not in self.list:
            raise KeyError('dict has not key: %s' % key)
        return self.get(key)

    def __delitem__(self, key):
        if key not in self.list:
            raise KeyError('dict has not key: %s' % key)
        self.list.remove(key)
        self.pop(key)

    def popitem(self, tail=True):
        """

        :param tail: True 最后一个元素 False 第一个元素
        :return:
        """
        if not self.list:
            raise KeyError('dict is empty')
        if tail:
            del self.list[-1]
            return self.get(self.list[-1])
        else:
            del self.list[0]
            return self.get(self.list[0])

    def __iter__(self):
        for key in self.list:
            yield key, self.get(key)

    def __str__(self):

        temp_list = []
        for key in self.list:
            value = self.get(key)

            temp_list.append("'%s':%s" % (key, value,))

        temp_str = '{' + ','.join(temp_list) + '}'
        return temp_str


if __name__ == "__main__":
    obj = SortedDict()
    obj["test"] = "test"
    obj["test1"] = "test1"
    obj["test2"] = "test2"
    obj["test3"] = "test3"
    for key, value in obj:
        print(key, value)
    print("test")
    del obj["test2"]
    print(obj)
    obj.popitem()
    print(obj)
