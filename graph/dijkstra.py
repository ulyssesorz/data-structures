def dijkstra(graph,start,end):
    """
    解决加权图的单源最短路径问题，是一种贪心算法
    """
    heap=[(0,start)]
    visited=[]
    while heap:
        heap.sort(key=lambda x:x[0],reverse=True)   #降序排列
        (cost,u)=heap.pop()                         #使用堆pop根节点（最小距离），此步包含了比较A-C和A-B-C的大小
        if u in visited:                            #跳过访问过的点
            continue
        if u==end:
            return cost
        visited.append(u)
        for v,c in graph[u]:              # v是与u相连的点，c是距离
            if v in visited:
                continue
            next=cost+c
            heap.append((next,v))        #该push把所有未遍历过的点都加到堆中，再通过pop比较，即原理中的”更新“步骤

if __name__ == '__main__':
	G = {
	    "A": [["B", 2], ["C", 5]],
	    "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
	    "C": [["A", 5], ["F", 3]],
	    "D": [["B", 3]],
	    "E": [["B", 4], ["F", 3]],
	    "F": [["C", 3], ["E", 3]],
	}
	print(dijkstra(G,'A','F'))