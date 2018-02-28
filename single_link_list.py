#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2018/2/27 16:45
"""


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_data(self, item):
        self.data = item

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def add_order(self, item):
        """
        有序链表添加
        :param item:
        :return:
        """
        current = self.head
        pre = None
        state = False
        while not state:
            if item <= current.get_data() and pre is None:
                state = True
            if item < current.get_data():
                state = True
            else:
                pre = current
                current = current.get_next()
        temp = Node(item)
        temp.set_next(current)
        pre.set_next(temp)

    def get(self, index):
        # 支持负数
        index = index if index >= 0 else len(self) + index
        if index < 0 or len(self) < index:
            return None
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        return pre

    def set(self, index, data):
        node = self.get(index)
        if node:
            node.set_data(data)
        return node

    def insert(self, index, data):
        """
        1.index 插入节点位置包括正负数
        2.找到index-1-->pre_node的节点
        3.pre_node.next-->node
          node.next-->pre_node.next.next
        4.head
        :param index:
        :param data:
        :return:
        """
        new_node = Node(data)
        if abs(index + 1) > len(self):
            return False
        index = index if index >= 0 else len(self) + index + 1
        if index == 0:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            pre_node = self.get(index-1)
            after_node = self.get(index)
            pre_node.set_next(new_node)
            new_node.set_next(after_node)
        return new_node

    def remove(self, item):
        current = self.head
        pre = None
        state = False
        while not state:
            if item == current.get_data():
                state = True
            else:
                pre = current
                current = current.get_next()
        if pre is None:
            self.head = current.get_next()
        else:
            pre.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def __reversed__(self):
        """
        1.pre-->next 转变为 next-->pre
        2.pre 若是head 则把 pre.nex --> None
        3.tail-->self.head
        :return:
        """
        def reverse(pre_node, node):
            if pre_node is self.head:
                pre_node.set_next(None)
            if node:
                next_node = node.get_next()
                node.set_next(pre_node)
                return reverse(node, next_node)
            else:
                self.head = pre_node
        return reverse(self.head, self.head.get_next())

    def __len__(self):
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    def __str__(self):
        pre = self.head
        list_all = []
        while pre:
            list_all.append(pre.get_data())
            pre = pre.next
        return str(list_all)


if __name__ == "__main__":
    single_link_list = UnorderedList()
    single_link_list.add(78)
    single_link_list.add(88)
    single_link_list.add(68)
    single_link_list.add(58)
    single_link_list.add(38)
    print(len(single_link_list))
    print(single_link_list.search(78))
    single_link_list.remove(88)
    print(single_link_list)
    print("set index = 1 -- data = 99")
    single_link_list.set(1, 99)
    print("get value index = 1")
    print(single_link_list.get(1).get_data())
    print(single_link_list)
    single_link_list.insert(1, 55)
    print("insert index = 1 -- data = 55")
    print(single_link_list)
    single_link_list.__reversed__()
    print(single_link_list)
