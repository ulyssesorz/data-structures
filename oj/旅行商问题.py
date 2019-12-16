"""
第一行输入旅行城市的数目m。（对应的城市编号为0~m-1）
第二行输入城市间的距离矩阵。
输出最短距离
"""
class TSP:
	def __init__(self,graph,start):
		self.graph=graph    #距离矩阵
		self.start=start    #出发的点

	def solve(self,node,sets):
		if len(sets)==0:                    #所有节点都已遍历过后，返回最后一个点到出发点的距离
			return self.graph[node][self.start]
		distance=[]
		for i in range(len(sets)):
			cur=sets[i]                     #选中一个节点
			temp=sets[:]                    #此处不能写成temp=sets，否则两者内存地址相同，恒相等
			temp.pop(i)                     #temp为未遍历的节点
			distance.append(self.graph[node][cur]+self.solve(cur,temp))     #solve递归找cur和未遍历节点的最短距离
		return min(distance)                #未遍历完所有节点时，返回此时的最小distance，即出发点到该点的最短距离

if __name__ == '__main__':
	g=[]
	n=int(input())
	for i in range(n):
		g.append(list(map(int,input().split(','))))

	sets = list(range(len(g)))
	sets.pop(sets.index(0))         # sets代表每个节点，不包括起始点
	tsp=TSP(g,0)
	print(tsp.solve(0,sets))