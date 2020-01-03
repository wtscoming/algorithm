'''
二叉树
列表之列表
'''
class Tree:
    # 创建根节点
    def __init__(self, r):
        self.root = [r, [], []]
    
    # 插入左节点
    def insert_left(self, new_branch):
        tmp = self.root.pop(1)
        # 原左子树成为新插入节点的左子树
        if len(tmp) > 1:
            self.root.insert(1, [new_branch, tmp, []])
        else:
            self.root.insert(1, [new_branch, [], []])
        # 返回插入完成的新树
        return self.root
    
    # 插入右节点
    def insert_right(self, new_branch):
        tmp = self.root.pop(2)
        if len(tmp) > 1:
            self.root.insert(2, [new_branch, [], tmp])
        else:
            self.root.insert(2, [new_branch, [], []])
        return self.root
    
    # 获取根节点
    def get_root(self):
        return self.root[0]
    
    # 设置根节点
    def set_root(self, new_val):
        self.root[0] = new_val
    
    # 获取左子树
    def get_left_child(self):
        return self.root[1]
    
    # 获取右子树
    def get_right_child(self):
        return self.root[2]
