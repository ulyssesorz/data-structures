"""
对于多邻点的顶点的遍历，按顶点值由低到高进行广度优先遍历。
第一行输入图的顶点总数目n，顶点依次编号为1，2…n，顶点编号即对应顶点值；第二行输入图的总边数m，
接下来m行输入每条边的两个顶点，以逗号分隔；最后输入遍历的始发顶点编号x。
"""
def bfs(graph,start):
	result,queue=[start],[start]
	while queue:
		v=queue.pop(0)                      #类似层序遍历的队列思想
		temp=[]
		for i in range(len(graph)):
			if v==graph[i][0] and graph[i][1] not in result:
				temp.append(graph[i][1])
		temp=sorted(temp)                   #按题目要求从小到大排列
		for i in temp:
			result.append(i)
			queue.append(i)
		temp=[]
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

	x=int(input())
	result=bfs(l,x)
	for i in result:
		print(i,end=' ')



