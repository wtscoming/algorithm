import sys
sys.path.append('..')

from my_package.Stack import Stack

# 将十进制数转化为二进制数
def binary_num(dec_num):
    rem = Stack()

    while dec_num > 0:
        rem.push(dec_num % 2)
        dec_num //= 2
    
    binary_string = ''
    while not rem.isEmpty():
        binary_string += str(rem.pop())
    
    return binary_string

# 将十进制数转化为任意进制数
def base_converter(dec_num, base):
    digits = '0123456789ABCDEF'
    rem = Stack()

    while dec_num > 0:
        rem.push(dec_num % base)
        dec_num //= base
    
    new_string = ''
    while not rem.isEmpty():
        new_string += digits[rem.pop()]
    
    return new_string
