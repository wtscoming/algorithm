from tests.make_change import make_change

# 读取一行整数
def read_ints():
    return tuple([int(x) for x in input().split(' ')])

if __name__ == '__main__':
    change = input()
    make_change(int(change))
    pass
