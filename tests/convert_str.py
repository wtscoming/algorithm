'''
将整数转换成任意进制的字符串
num { int } 整数
base { int } 进制
'''

base_value = '0123456789ABCDEF'

def convert_str(num, base):
    if num < base:
        return base_value[num]
    return convert_str(num // base, base) + convert_str(num % base, base)
