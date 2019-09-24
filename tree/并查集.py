class UnionFind:
    def __init__(self,n):
        self.uf=[-1 for i in range(n+1)]
        self.count=n

    def find(self,p):
        if self.uf[p]<0:
            return p
        else:
            self.uf[p]=self.find(uf[p])
        return self.uf[p]                       #返回根节点的子节点

    def union(self,p,q):
        proot=self.find(p)
        qroot=self.find(q)

        if self.uf[proot]==self.uf[qroot]:
            return
        elif self.uf[proot]>self.uf[qroot]:         #两者都为负数
            self.uf[qroot]+=self.uf[proot]          #大小相加
            self.uf[proot]=qroot                    #把qroot当成proot的父节点
        else:
            self.uf[proot]+=self.uf[qroot]
            selfuf[qroot]=proot
        self.count-=1

    def is_connect(self,p,q):
        return self.find(p)==self.find(q)

