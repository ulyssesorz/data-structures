"""
现有一个班级上课老师要求同学们做汇报，老师先选取做汇报的人数（至多十个同学），再以学号进行选择（学号范围为0～9999），
并按照一定规则填入哈希表，以其在哈希表的位置从小到大做课程汇报。规则如下：先将学号各个位数相加，
如学号2333，2+3+3+3=11，则关键字记为11，若同时又有学号为3332的同学被选中，3+3+3+2=11，此时关键字记为111，
学号为3233的同学关键字记为211，也就是说当各位数相加所得值相同时，则关键字在百位数依次加一。哈希表的长度为汇报同学的人数，
输入数据共有两行。第一行为做汇报同学的人数，第二行为汇报的同学的学号，每个学号之间用一个空格隔开
输出为排序后的列表，列表中各元素对应排序后的学号
"""
class HashTable:
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


def count(n):           #将学号转化为指定形式
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

def times(li,n):        #计算列表中某元素出现的次数
    cou=0
    for i in li:
        if i==n:
            cou+=1
    return cou

if __name__ == '__main__':
    n=int(input())
    li=list(map(int,input().split()))
    ht=HashTable(n)
    c=[]
    res=[]
    for i in li:
        temp=count(i)
        cou=times(c,temp)
        c.append(temp+cou*100)              #得到转化后的学号列表c
    for i in c:
        ht.insert(i)
    for i in ht.data:
        if i:
            res.append(li[c.index(i)])      #按c的索引顺序
    print(res)