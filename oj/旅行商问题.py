"""
第一行输入旅行城市的数目m。（对应的城市编号为0~m-1）
第二行输入城市间的距离矩阵。
输出最短距离
"""
def tsp(node,set):
	if len(set)==0:
		return graph[node][start]   #所有节点都已遍历过后，返回最后一个点到出发点的距离
	distance=[]
	for i in range(len(set)):
		cur=set[i]              #选中一个节点
		others=set[:]           #此处不能写成others=set，否则两者内存地址相同，恒相等
		others.pop(i)           #others为未遍历的节点
		distance.append(graph[node][cur]+tsp(cur,others))   #tsp递归找cur和未遍历节点的最短距离
	return min(distance)        #未遍历完所有节点时，返回此时的最小distance，即出发点到该点的最短距离

if __name__ == '__main__':
	start=0             #起始节点
	graph=[]
	n=int(input())
	for i in range(n):
		graph.append(list(map(int,input().split(','))))
	set=list(range(len(graph)))
	set.pop(set.index(start))       # set代表每个节点，不包括起始点
	print(tsp(start,set))