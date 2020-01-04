"""
八皇后问题的递归解法
"""
def eight_queen(queen):
    if len(queen)==8:
        return [queen]          #拍到最后一行，返回一种结果
    else:
        return sum([eight_queen(queen+[i]) for i in range(8) if is_valid(queen+[i])],[])        #每次递归都嵌套在一个列表中，sum的作用是去除多余的外层列表

def is_valid(queen):            #检查是否符合规则
    if len(set(queen))!=len(queen):
        return False
    for i,q in enumerate(queen):
        for i2,q2 in enumerate(queen):
            if i==i2:
                continue        #同一个位置，不需要进行下面的比较
            d=i-i2
            if q2==q-d or q2==q+d:  #两个位置的行号差值等于列号差值的绝对值，说明在同一斜线上
                return False
    return True

if __name__ == '__main__':
    print(len(eight_queen([])))


