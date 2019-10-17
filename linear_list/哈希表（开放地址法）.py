class HashTable:
    """
    采用除留余数法（H（key）=key %n）建立长度为n的哈希表，处理冲突用开放定址法的线性探测，
    有冲突时：H = H(key)+d） %n,d=1,2,3...
    第一行为哈希表的长度n；第二行为关键字集合；第三行为要查找的数据。
    """
    def __init__(self,size):
        self.size=size              #哈希表长度
        self.data=[None]*self.size

    def hash(self,key):
        return key%self.size

    def solution(self,key):
        return (self.hash(key)+1)%self.size     #开放定制法（线性探测）

    def insert(self,data):
        value=self.hash(data)
        if self.data[value] is None:
            self.data[value]=data
        else:
            next=self.solution(data)
            while self.data[next] is not None:
                next=self.solution(next)
                if next>=self.size:
                    next=0
            self.data[next]=data

    def search(self,data):
        value=self.hash(data)
        count=0
        while self.data[value] is not None:
            if self.data[value]==data:      #找到data，返回比较次数
                return count+1
            else:
                value=self.solution(value)
                count+=1
        if self.data[value] is None:        #到None仍未找到data，说明其不在表中，返回-1
            return -1

if __name__=='__main__':

    length=int(input())
    h=HashTable(length)

    list=input().split()
    list=[int(i) for i in list]
    for i in list:
        h.insert(i)

    print(h.data)               #输出哈希表
    print(h.search(int(input())))   #输出比较次数

# e.g  11
#      47 7 29 11 9 84 54 20 30
#      30

# ans  [11, 54, 20, 47, 30, None, None, 7, 29, 9, 84]
#      8
