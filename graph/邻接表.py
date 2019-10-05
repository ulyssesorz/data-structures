class AdjacencyList:
    def __init__(self):
        self.list={}

    def add_edge(self,fromvertex,tovertex):
        if fromvertex in self.list.keys():
            self.list[fromvertex].append(tovertex)       #键已存在，把链接的节点存在键值(一个列表)里
        else:
            self.list[fromvertex]=[tovertex]             #键不存在，直接把节点转化为列表当成新键值

    def print_list(self):
        for i in self.list:
            print(i,'->',' -> '.join(str(j) for j in self.list[i])) 

al = AdjacencyList()
al.add_edge(0, 1)
al.add_edge(0, 4)
al.add_edge(4, 1)
al.add_edge(4, 3)
al.add_edge(1, 0)
al.add_edge(1, 4)
al.add_edge(1, 3)
al.add_edge(1, 2)
al.add_edge(2, 3)
al.add_edge(3, 4)

al.print_list()