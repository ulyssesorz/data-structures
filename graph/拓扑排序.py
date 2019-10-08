def topological_sort(graph):
    """
    一种将图转化为线性结构的方法
    要求：
        1、每个顶点出现且只出现一次。
        2、若A在序列中排在B的前面，则在图中不存在从B到A的路径。
    """
    indegree=[0]*len(graph)
    queue=[]
    topo=[]
    count=0

    for key,value in graph.items():
        for i in value:
            indegree[i]+=1          #计算每个节点的入度，入度为0说明未被其他节点指向

    for i in range(len(indegree)):
        if indegree[i]==0:
            queue.append(i)         #入度为0的点放入队列中

    while queue:
        vertex=queue.pop(0)
        topo.append(vertex)
        count+=1                    #统计pop的点的个数，判断是否成环
        for i in graph[vertex]:
            indegree[i]-=1                 #删掉一个节点后，其子节点的入度减1，
            if indegree[i]==0:
                queue.append(i)

    if count!=len(graph):           #存在点入度恒不为0
        print('Cycle')
    else:
        print(topo)

G = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}
topological_sort(G)
G2 = {0: [1, 2], 1: [0,2], 2: [0,1]}
topological_sort(G2)


