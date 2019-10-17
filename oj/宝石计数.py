class HashTable:
    """
    输入：bKA
          bBBBaAAKKzzmmkkk
    输出：5
    即下面字符串含有上面字符的数目
    """
    def __init__(self):
        self.treasure=[None]*100                   #用于存斜率

    def ascii(self,c):                  #将字符转化为ascii码
        return ord(c)

    def hash(self,data):
        return self.ascii(data)%10

    def solution(self,data):
        return self.ascii(data)%10+1

    def insert(self,data):
        value=self.hash(data)
        if self.treasure[value]==None:
            self.treasure[value]=self.ascii(data)
        else:
            next=self.solution(data)
            while self.treasure[next]!=None:
                next+=1
                if next>199:
                    next=0                             #到表的尽头后从头开始找
            self.treasure[next]=self.ascii(data)           #找到空的地方插入

    def search(self,data):
        count=0
        a=self.ascii(data)
        for i in range(100):
            if self.treasure[i]==a:
                count+=1
        return count


h=HashTable()
type=input()
stones=input()
for i in stones:
    h.insert(i)
n=0
for i in type:
    n+=h.search(i)
print(n)