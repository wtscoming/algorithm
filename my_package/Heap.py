'''
堆
二叉小顶堆, 注: 下标从1开始
'''
class Heap:
    def __init__(self):
        self.items = [0]
    
    # 堆的尺寸: 0不计算在内
    def size(self):
        return len(self.items) - 1
    
    # 向上调整小顶堆
    def percUp(self, i):
        while i // 2 > 0:
            if self.items[i] < self.items[i // 2]:
                self.items[i], self.items[i // 2] = self.items[i // 2], self.items[i]
            i //= 2
    
    # 插入元素
    def insert(self, k):
        self.items.append(k)
        self.percUp(self.size())
    
    # 向下调整小顶堆
    def percDown(self, i):
        while i * 2 <= self.size():
            min_child = i * 2
            if min_child + 1 <= self.size() and \
                self.items[min_child + 1] < self.items[min_child]:
                min_child += 1
            if self.items[i] > self.items[min_child]:
                self.items[i], self.items[min_child] = self.items[min_child], self.items[i]
            i = min_child
    
    # 获取堆顶(最小)元素
    def top(self):
        if self.size() == 1:
            return self.items.pop()
        tmp = self.items[1]
        self.items[1] = self.items.pop()
        self.percDown(1)
        return tmp
    
    # 根据元素列表构建堆
    def build(self, alist):
        self.items = [0] + alist[:]
        i = self.size() // 2
        while i > 0:
            self.percDown(i)
            i -= 1
