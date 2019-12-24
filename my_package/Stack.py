'''
栈
items { list } 栈的元素
'''
class Stack:
    def __init__(self):
        self.items = []
    
    # 栈是否为空
    def isEmpty(self):
        return len(self.items) == 0
    
    # 压栈
    def push(self, item):
        self.items.append(item)
    
    # 出栈
    def pop(self):
        return self.items.pop()
    
    # 取栈顶元素
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    # 栈的大小
    def size(self):
        return len(self.items)