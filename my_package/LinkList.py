'''
链表
head { Node } 头指针
'''
import sys
sys.path.append('..')

from my_package.Node import Node

class LinkList:
    def __init__(self):
        self.head = None
    
    # 链表是否为空
    def isEmpty(self):
        return self.head == None
    
    # 添加元素(头插法)
    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node
    
    # 链表长度
    def length(self):
        current = self.head
        counter = 0

        while current != None:
            current = current.get_next()
            counter += 1
        
        return counter
    
    # 查找元素
    def search(self, item):
        current = self.head
        
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        
        return False
    
    # 移除元素
    def remove(self, item):
        prev = self.head
        next = prev.get_next()
        while next != None:
            if next.get_data() == item:
                break
            prev = next
            next = next.get_next()

        if next != None:
            prev.set_next(next.get_next())
            del next
    
    # 添加元素
    def append(self, item):
        rear = self.head
        while rear.get_next() != None:
            rear = rear.get_next()
        rear.set_next(Node(item))
    
    # 插入元素
    def insert(self, index, item):
        current = self.head
        counter = 0

        while counter < index and current.get_next() != None:
            current = current.get_next()
            counter += 1
        
        node = Node(item)
        node.set_next(current.get_next())
        current.set_next(node)
    
    # 查找索引
    def index(self, item):
        current = self.head
        index = 0

        while current.get_next() != None:
            if current.get_next().get_data() == item:
                return index
            current = current.get_next()
            index += 1
        
        return None
    
    # 弹出最后一个节点
    def pop(self):
        prev = self.head
        next = prev.get_next()

        while next != None:
            prev = next
            next = next.get_next()
        
        prev.set_next(None)
        return next
