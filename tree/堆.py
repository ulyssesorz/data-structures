class Heap:
    def __init__(self):
        self.h=[]
        self.size=0

    def leftchild(self,i):
        if 2*i+1<self.size:
            return 2*i+1
        return None

    def rightchild(self, i):
        if 2 * i + 2 < self.size:
            return 2 * i + 2
        return None

    def maxheap(self,node):
        if node<self.size:
            m=node
            le=self.leftchild(node)
            ri=self.rightchild(node)
            if le is not None and self.h[le]>self.h[m]:
                m=le
            if ri is not None and self.h[ri]>self.h[m]:
                m=ri                                        #两个if语句找出了父节点和两个子节点中的值最大者的索引
            if m!=node:
                self.h[m],self.h[node]=self.h[node],self.h[m]       #交换，把值最大者放在父节点
                self.maxheap(m)                              #交换后的子节点可能不满足堆的要求，故对其maxheap

    def buildheap(self,a):
        self.h=list(a)
        self.size=len(a)          #初始化
        for i in range(self.size//2,-1,-1):               #遍历每个父节点，对其最大堆构造
            self.maxheap(i)

    def getmax(self):
        if self.size>=1:
            max=self.h[0]
            self.h[0],self.h[self.size-1]=self.h[self.size-1],self.h[0]   #最后一个节点接到0位置，保持堆的结构
            self.size-=1
            self.maxheap(0)
            return max
        return None

    def insert(self,data):
        sizet=self.size
        self.h.append(data)
        self.size+=1
        while self.h[sizet]>self.h[(sizet-1)//2]:
            self.h[sizet],self.h[(sizet-1)//2]=self.h[(sizet-1)//2],self.h[sizet]         #从最后一个节点向上交换
            sizet=(sizet-1)//2

    def display(self):
        print(self.h)


h=Heap()
l = list(map(int, input().split()))
h.buildheap(l)
h.insert(2)
print(h.getmax())
h.display()

