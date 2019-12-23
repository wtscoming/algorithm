'''
分数类型
top { int } 分子
bottom { int } 分母
'''
class Fraction(object):
    def __init__(self, top, bottom):
        super().__init__()
        # 分母为负数时
        if bottom < 0:
            self.top = -top
        else:
            self.top = top
        self.bottom = abs(bottom)
    
    def show(self):
        print(str(self.top) + '/' + str(self.bottom))
    
    def __str__(self):
        return str(self.top) + '/' + str(self.bottom)
    
    # 最大公约数
    @staticmethod
    def gcd(self, m, n):
        '''
        while m % n != 0:
            old_m = m
            old_n = n
            m = old_n
            n = old_m % old_n
        return n
        '''
        if m % n == 0:
            return n
        return Fraction.gcd(self, n, m % n)
    
    # 分数加分
    def __add__(self, value):
        top = self.top * value.bottom + self.bottom * value.top
        bottom = self.bottom * value.bottom
        # 化为最简分数
        gcd = Fraction.gcd(self, top, bottom)
        return Fraction(top // gcd, bottom // gcd)
    
    pass