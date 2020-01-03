'''
二叉树
节点与引用
'''
class BinaryTree(object):
    # 创建根节点
    def __init__(self, root, left = None, right = None):
        super().__init__()
        self.root = root
        self.left = left
        self.right = right
    
    # 插入左节点
    def insert_left(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            self.left = BinaryTree(node, self.left)
    
    # 插入右子树
    def insert_right(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            self.right = BinaryTree(node, None, self.right)
    
    # 二叉树的访问函数
    def get_root(self):
        return self.root
    
    def set_root(self, node):
        self.root = node
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    # 先序遍历
    @staticmethod
    def pre_order(root, level = 0):
        if root == None:
            return
        for i in range(level):
            print('', end='\t')
        print(root.get_root())
        BinaryTree.pre_order(root.get_left(), level + 1)
        BinaryTree.pre_order(root.get_right(), level + 1)

    '''
    内部遍历方法
    def _pre_order(self):
        print(self.root)
        if self.left:
            self.left._pre_order()
        elif self.right:
            self.right._pre_order()
    '''
