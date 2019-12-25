'''
双端队列
items { list } 双端队列元素
'''
class Deque:
    def __init__(self):
        self.items = []

    # 双端队列是否为空
    def isEmpty(self):
        return len(self.items) == 0
    
    # 在队头添加元素
    def add_front(self, item):
        self.items.insert(0, item)
    
    # 在队尾添加元素
    def add_rear(self, item):
        self.items.push(item)
    
    # 移除队头元素
    def remove_front(self):
        return self.items.pop(0)
    
    # 移除队尾元素
    def remove_rear(self):
        return self.items.pop()
    
    # 双端队列大小
    def size(self):
        return len(self.items)
