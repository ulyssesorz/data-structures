G = [
    [0, 1, 2],
    [3, 0, 6],
    [1, 3, 0],
]

def printdis(graph):
    for i in graph:
        print(i)

def floyd(graph):
    """
    比较i-j和i-n-j的大小（n为1,2,3，...），更新最短路径
    解决多源图的最短路径问题
    该简化版重在5行核心代码，忽略不连通等情况
    """
    n=len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j]>graph[i][k]+graph[k][j]:
                    graph[i][j]=graph[i][k]+graph[k][j]
    return graph

printdis(floyd(G))