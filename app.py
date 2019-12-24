from tests.binary_num import base_converter

# 读取一行整数
def read_ints():
    return tuple([int(x) for x in input().split(' ')])

if __name__ == '__main__':
    dec_num, base = read_ints()
    print(base_converter(dec_num, base))
