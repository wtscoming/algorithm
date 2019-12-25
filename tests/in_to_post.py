'''
中序表达式转后续表达式
string.ascii_uppercase { string } 用大写字母表示操作数
'''
import sys
sys.path.append('..')

from my_package.Stack import Stack
import string

def in_to_post(in_string):
    # 操作符优先级字典
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2

    op_stack = Stack()
    post_string = ''

    for item in in_string:
        # 操作数直接输出
        if item in string.ascii_uppercase:
            post_string += item
        # 左括号优先级最低
        elif item == '(':
            op_stack.push(item)
        # 右括号需要一直匹配到左括号(左括号也需要出栈)
        elif item == ')':
            '''
            while not op_stack.peek() == '(':
                post_string += op_stack.pop()
            op_stack.pop()
            '''
            peek_token = op_stack.pop()
            while peek_token != '(':
                post_string += peek_token
                peek_token = op_stack.pop()
        # 操作符比较优先级
        else:
            while not op_stack.isEmpty() and prec[op_stack.peek()] >= prec[item]:
                post_string += op_stack.pop()
            op_stack.push(item)
    
    # 将剩下的操作符出栈
    while not op_stack.isEmpty():
        post_string += op_stack.pop()
    
    return post_string
