'''
https://leetcode-cn.com/problems/24-game/description/
679. 24点游戏
你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。

示例 1:

输入: [4, 1, 8, 7]
输出: True
解释: (8-4) * (7-1) = 24
示例 2:

输入: [1, 2, 1, 2]
输出: False
注意:

除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
'''

class Operator(object):
    def realNum(self, x):
        return x() if callable(x) else x


class Add(Operator):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.realNum(self.x) + self.realNum(self.y) 

    def __str__(self):
        return '({0} + {1})'.format(self.x,self.y)

class Minus(Operator):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.realNum(self.x) - self.realNum(self.y)

    def __str__(self):
        return '({0} - {1})'.format(self.x,self.y)

class _Minus(Operator):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.realNum(self.y) - self.realNum(self.x)

    def __str__(self):
        return '({1} - {0})'.format(self.x,self.y)

class Mul(Operator):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.realNum(self.x) * self.realNum(self.y)

    def __str__(self):
        return '{0} * {1}'.format(self.x,self.y)

class Div(Operator):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.realNum(self.x) / self.realNum(self.y)

    def __str__(self):
        return '{0} / {1}'.format(self.x,self.y)

class _Div(Operator):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.realNum(self.y) / self.realNum(self.x)

    def __str__(self):
        return '{1} / {0}'.format(self.x,self.y)

calculate = [Add, Minus, _Minus, Mul, Div, _Div]

def canGet24(card):

    try:
        if len(card) == 1:
            if(abs(24- card[0]()) < 0.0000000000001):
                str = card[0].__str__()
                if str[0]=='(':
                    str = str[1:-1]
                print(str)
                return True
            else:
                return False
        if len(card) == 2:
            # return card[0]+card[1] == 24 or card[0]-card[1]==24 or card[1]-card[0]==24 or card[0] * card[1]==24 or card[0]/card[1]==24 or card[1]/card[0]==24
            for fun in calculate:
                if canGet24([fun(card[0],card[1])]) == True:
                    return True
            return False

        if len(card) == 3:
            for fun in calculate:
                x,y,z = card
                if canGet24([x,fun(y,z)]) == True:
                    return True
                if canGet24([y,fun(x,z)]) == True:
                    return True
                if canGet24([z,fun(x,y)]) == True:
                    return True
            return False
        for fun in calculate:
            a,b,c,d = card
            if canGet24([fun(a,b),c,d]) == True:
                return True
            if canGet24([fun(a,c),b,d]) == True:
                return True
            if canGet24([fun(a,d),b,c]) == True:
                return True
            if canGet24([fun(b,c),a,d]) == True:
                return True
            if canGet24([fun(b,d),a,c]) == True:
                return True
            if canGet24([fun(c,d),a,b]) == True:
                return True
        return False
    except ZeroDivisionError:
        return False
    

def main():
    print(canGet24([4,1,8,7]))

if __name__ == '__main__':
    main()