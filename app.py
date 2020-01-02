from my_package.Sort import Sort

# 读取一行整数
def read_ints():
    return tuple([int(x) for x in input().split(' ')])

if __name__ == '__main__':
    alist = [5, 4, 3, 2, 1]
    blist = Sort.quick_sort(alist)
    print(blist)
