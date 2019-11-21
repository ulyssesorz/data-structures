"""
输入第一行为正整数N。（N>0）N为图的节点数。接下来输入一个N行N列的矩阵C，因为是无向图，
所以这是一个沿对角线对称的矩阵，矩阵的元素Cij代表从i节点到j节点的花费值。PS：若该条边不存在，则设置数值为65535.
输出一个数字，最小生成树的cost。
"""
def prim(graph):
	node_num=len(graph)         #点的数目
	edge_num=0
	for i in range(node_num):   #遍历半个矩阵，两点连通则有一条边
		for j in range(i):
			if graph[i][j]<65535:
				edge_num+=1

	res=[]
	if node_num<=0 or edge_num<node_num-1:
		return res
	selected_node=[0]           #已选择的节点
	candidate_node=[i for i in range(1,node_num)]   #待选的节点

	while len(candidate_node)!=0:
		begin,end,min=0,0,65535
		for i in selected_node:         #找到与已选节点相连的相连的最短边
			for j in candidate_node:
				if graph[i][j]<min:
					begin=i
					end=j
					min=graph[i][j]
		res.append(min)
		selected_node.append(end)       #已选节点之间不可能连通，避免形成回路
		candidate_node.remove(end)
	return res

if __name__ == '__main__':
	n=int(input())
	graph=[]
	for i in range(n):
		graph.append(list(map(int, input().split())))
	weight=prim(graph)
	print(sum(weight))
