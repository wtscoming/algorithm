'''
约瑟夫环问题：队列模拟解法
'''
import sys
sys.path.append('..')

from my_package.Queue import Queue

# 名字列表中的人每次报数num, 第num个人出局, 返回最后剩下的一个
def josephus(name_list, num):
    q = Queue()

    # 初始化
    for name in name_list:
        q.en_queue(name)
    
    while q.size() > 1:
        for i in range(num):
            q.en_queue(q.de_queue())
        # 第num个人此时位于队头
        q.de_queue()
    
    return q.de_queue()
