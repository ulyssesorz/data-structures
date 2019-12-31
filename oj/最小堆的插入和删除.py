"""
第一行是一个数组，代表了最小堆。第二行是接下来要进行操作的次数。第三行开始，分别是两种操作，
I代表插入，D代表删除。如果操作是I的话，接下去会紧跟一行待插入的数字
一行，经过插入和删除后的最小堆，直接输出list即可。
"""
class Heap:
	def __init__(self):
		self.h = []
		self.size = 0

	def leftchild(self, i):         #返回左节点的索引
		if 2 * i + 1 < self.size:
			return 2 * i + 1
		return None

	def rightchild(self, i):        #返回右节点的索引
		if 2 * i + 2 < self.size:
			return 2 * i + 2
		return None

	def minheap(self, i):
		if i >= self.size:
			return
		m = i
		left = self.leftchild(m)
		right = self.rightchild(m)
		if left and self.h[left] < self.h[m]:
			m=left
		if right and self.h[right]<self.h[m]:
			m=right
		if m!=i:                                    #此时的m是三个节点中最小的节点的索引
			self.h[m],self.h[i]=self.h[i],self.h[m]
			self.minheap(m)

	def buildheap(self,list):
		self.h=list
		self.size=len(list)
		for i in range(self.size//2,-1,-1):            #依次最小化堆
			self.minheap(i)

	def insert(self,val):
		sizet=self.size
		self.size+=1
		self.h.append(val)
		while self.h[sizet]<self.h[sizet//2]:           #向上比较节点和父节点的大小，若不符最小堆特点则交换
			self.h[sizet],self.h[sizet//2]=self.h[sizet//2],self.h[sizet]
			sizet//=2

	def delete(self):           #删除根节点：即把最后一个节点和根节点交换，再删除最后一个节点
		if self.size==0:        #防止溢出
			return
		self.h[self.size-1],self.h[0]=self.h[0],self.h[self.size-1]
		self.h.pop()
		self.size-=1
		self.minheap(0)

if __name__ == '__main__':
	h = Heap()
	l = list(map(int, input().split()))
	h.buildheap(l)
	n = int(input())
	for i in range(n):
		op = input()
		if op == 'D':
			h.delete()
		elif op == 'I':
			li = list(map(int, input().split()))
			for i in li:
				h.insert(i)
	print(h.h)