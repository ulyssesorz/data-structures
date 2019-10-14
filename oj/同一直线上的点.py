class HashTable:
    def __init__(self):
        """
        现在输入N个平面坐标系上点，每个点均是过原点的直线（形如y=kx，k为int型，0<k<100）上的点，
        现要求判断这组输入的点的坐标之中，最多有几个点是在同一条y=kx直线上。PS:每组测试用例中不同斜率k的个数不超过10，
        要求使用size不超过10的哈希表来储存k。使用线性探测法解决冲突。
        首先输入的是点的数量N,接下来是N行数据，每行都是一个点的坐标。
        """
        self.rake=[0]*200                   #用于存斜率

    def raked(self,coor):
        return coor[1]//coor[0]

    def hash(self,coor):
        return self.raked(coor)%10

    def solution(self,coor):
        if self.raked(coor)%10>198:
            return 1
        else:
            return self.raked(coor) % 10 + 1        #冲突解决：线性检测，向后退一位

    def insert(self,data):
        if data[0]==0 and data[1]==0:      #特殊点（0,0)不能用hash处理，直接把斜率1放入rake
            j=0
            while self.rake[j]!=0:
                j+=1
            self.rake[j]=1
            return

        value=self.hash(data)
        if self.rake[value]==0:
            self.rake[value]=self.raked(data)
        else:
            next=self.solution(data)
            while self.rake[next]!=0:
                next+=1
                if next>199:
                    next=0                             #到表的尽头后从头开始找
            self.rake[next]=self.raked(data)           #找到空的地方插入

    def find_max(self):
        max=0
        for i in self.rake:
            if self.rake.count(i)>max and i!=0:        #找到出现次数最多的斜率
                max = self.rake.count(i)
        return max

h=HashTable()
n=int(input())
for i in range(n):
    list=input().split()
    list=[int(i) for i in list]
    h.insert(list)

print(h.find_max())
