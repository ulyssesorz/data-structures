"""
一个“快乐数”定义为:对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程。若这个数最终可以变为1，
则这个数字是快乐数。但也可能是无限循环但始终变不到1，则不是快乐数。
例如: 数字19经过替换，依次为1^2+9^2=82，8^2+2^2=68，6^2+8^2= 100，1^2+0^2+0^2=1。 所以19为一个快乐数
"""
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [[] for i in range(self.size)]

    def hash(self,key):
        return key%len(self.slots)

    def insert(self,data):
        key=self.hash(data)
        if data in self.slots[key]:         #出现重复，将无限循环，不是快乐数
            return True
        self.slots[key].append(data)
        return False

def happy(n):
    sum=0
    for i in str(n):
        sum+=(int(i))**2
    return sum

if __name__ == '__main__':
    ht=HashTable(200)
    n=int(input())
    if happy(n)==1:
        print('True')
    else:
        while n != 1:
            n = happy(n)
            if ht.insert(n):
                print('False')
                break
            if n == 1:
                print('True')
                break