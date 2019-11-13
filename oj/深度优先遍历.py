"""
从节点1开始。同时由于图的深度优先遍历不唯一，我们约定对于多邻点的顶点的遍历，按顶点值由低到高进行深度优先遍历。
第一行输入图的顶点的数目；第二行输入图的边数；接下来逐行输入边。
eg: 4
	4
	1,2  1,3  1,4  3,4 (每条边换行)
"""
def dfs(graph):
	result = []
	stack = [1]
	while stack:
		v = stack.pop()
		if v in result:
			continue
		result.append(v)
		temp = []
		for i in range(len(graph)):
			if graph[i][0] == v and graph[i][1] not in result:
				temp.append(graph[i][1])                #先收集节点i的邻节点，为满足题目要求，需对其降序排列
		temp = sorted(temp, reverse=True)
		for i in temp:
			stack.append(i)
		temp = []
	return result

if __name__ == '__main__':
	n = input()             #无用，骗骗oj
	m = int(input())
	l = []

	for i in range(m):
		l.append(list(map(int, input().split(','))))

	count = 0
	length = len(l)
	for item in l:
		l.append([item[1], item[0]])        #写出其对称闭包，因为是无向图，有[1,3]就要有[3,1]
		count += 1
		if count == length:                 #设置次数，防止无限循环
			break

	result=dfs(l)
	for i in result:
		print(i,end=' ')



