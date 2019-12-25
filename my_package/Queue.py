'''
队列
items { list } 队列里的元素
索引小的方向为队头
'''
class Queue:
    def __init__(self):
        self.items = []
    
    # 队列是否为空
    def isEmpty(self):
        return len(self.items) == 0
    
    # 元素入队列
    def en_queue(self, item):
        self.items.append(item)
    
    # 元素出队列
    def de_queue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)
    
    # 队列大小
    def size(self):
        return len(self.items)
