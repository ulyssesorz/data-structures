"""
第一行是图的节点数n。第二行到第n+1行，是对应的图的邻接矩阵。如果两个节点之间不存在边，则输入数据为65535。
输出一行，代表从所有节点（包含第一个节点自己）到第一个节点的最短路径的长度。
"""
def floyed(graph):      #弗洛伊德算法得出所有最短路径
	n=len(graph)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if graph[i][j]>graph[i][k]+graph[k][j]:
					graph[i][j] = graph[i][k] + graph[k][j]
	return graph

if __name__ == '__main__':
	n=int(input())
	g=[]
	for i in range(n):
		g.append(list(map(int, input().split())))
	print(floyed(g)[0])