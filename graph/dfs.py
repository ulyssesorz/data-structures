G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

def dfs(graph,start):
    """
    深度优先遍历，类似树的先序遍历，一路向下找，用栈实现
    """
    result,stack=[],[start]

    while stack:
        v=stack.pop()                  #此句是区别bfs的关键，pop(0)是从头开始，即一圈一圈地遍历，pop()是从新加入的节点开始，即一路向下遍历
        if v in result:                #节点已在result中，不需进行后面的操作
            continue
        result.append(v)
        for i in graph[v]:
            if i not in result:
                stack.append(i)
    return result

print(dfs(G,'A'))
print(dfs(G,'B'))