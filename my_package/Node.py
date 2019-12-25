'''
链表节点类
data { any } 数据域
next { Node } 指针域
'''
class Node:
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next
    
    # 获取数据
    def get_data(self):
        return self.__data
    
    # 获取下一个节点
    def get_next(self):
        return self.__next
    
    # 设置数据
    def set_data(self, data):
        self.__data = data
    
    # 设置指针域
    def set_next(self, next):
        self.__next = next
