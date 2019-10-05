G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

def bfs(graph,start):
    """
    广度优先遍历，类似树的层次遍历，一层一层进行
    """
    result,queue=[start],[start]
    while queue:
        v=queue.pop(0)             #v是节点
        for i in graph[v]:
            if i not in result:
                result.append(i)
                queue.append(i)
    return result

if __name__=='__main__':
    print(bfs(G,'A'))
    print(bfs(G,'B'))