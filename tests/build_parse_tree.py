'''
构建树解析器
访问父节点需要使用栈
'''
import sys
sys.path.append('..')

from my_package.Stack import Stack
from my_package.BinaryTree import BinaryTree

def build_parse_tree(alist):
    s = Stack()
    t = BinaryTree('')
    current_tree = t
    for item in alist:
        # 添加一个左子节点, 并下沉至该节点
        if item == '(':
            current_tree.insert_left('')
            s.push(current_tree)
            current_tree = current_tree.get_left()
        # 右括号返回父节点
        elif item == ')':
            current_tree = s.pop()
        # 设置当前节点为操作符, 添加一个右子节点, 并下沉至该节点
        elif item in '+-*/':
            current_tree.set_root(item)
            current_tree.insert_right('')
            s.push(current_tree)
            current_tree = current_tree.get_right()
        # 将当前节点设为数字并返回至父节点
        else:
            current_tree.set_root(eval(item))
            current_tree = s.pop()
    return t
