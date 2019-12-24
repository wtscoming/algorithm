import sys
sys.path.append('..')

from my_package.Stack import Stack

# 匹配任意括号
def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

# 匹配小括号符号串
def pair_check(symbol_string):
    s = Stack()
    for item in symbol_string:
        # 左括号直接入栈
        if item == '(':
            s.push(item)
        # 右括号需要与左括号匹配
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
    return s.isEmpty()

# 匹配任意括号符号串
def any_pair_check(symbol_string):
    s = Stack()
    for item in symbol_string:
        if item in '([{':
            s.push(item)
        else:
            if s.isEmpty():
                return False
            else:
                # 取出左括号
                peek = s.pop()
                # 如果左右括号类型不匹配
                if not matches(peek, item):
                    return False
    return s.isEmpty()