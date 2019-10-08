class Graph:
    def __init__(self,graph):
        self.graph=graph
        self.node_num = self.get_node_num()          #顺序和下面两个函数的顺序一致
        self.edge_num=self.get_edge_num()

    def get_node_num(self):
        return len(self.graph)

    def get_edge_num(self):
        count=0
        for i in range(self.node_num):
            for j in range(i):
                if self.graph[i][j]>0 and self.graph[i][j]<9999:    #遍历半个矩阵，两点连通则边数加一
                    count+=1
        return count

    def kruskal(self):
        """
        图的最小生成树问题，原理是“找边”
        """
        res=[]
        if self.node_num<=0 or self.edge_num<self.node_num-1:
            return res
        edge_list=[]
        for i in range(self.node_num):
            for j in range(i,self.node_num):
                if self.graph[i][j]<9999:
                    edge_list.append([i,j,self.graph[i][j]])             #构造所有边的集合
        edge_list.sort(key=lambda a:a[2])                            #按照边的权值大小排序，为了后面按顺序先选最小边
        node_list=[[i] for i in range(self.node_num)]                #构造所有点的集合

        for edge in edge_list:                       #遍历每条边
            for i in range(len(node_list)):
                if edge[0] in node_list[i]:     #标记父节点对应点的下标
                    m=i
                if edge[1] in node_list[i]:     #标记子节点对应点的下标
                    n=i
            if m!=n:                            #不在同一集合里，说明不都是父节点，可添加到res
                res.append(edge)
                node_list[m]=node_list[m]+node_list[n]      #已确定的边，将其两个节点合并到一个集合中(视作父节点)，避免节点连接两次产生回路
                node_list[n]=[]
        return res

if __name__=='__main__':
    max_value = 9999
    row0 = [0, 7, max_value, max_value, max_value, 5]
    row1 = [7, 0, 9, max_value, 3, max_value]
    row2 = [max_value, 9, 0, 6, max_value, max_value]
    row3 = [max_value, max_value, 6, 0, 8, 10]
    row4 = [max_value, 3, max_value, 8, 0, 4]
    row5 = [5, max_value, max_value, 10, 4, 0]
    maps = [row0, row1, row2, row3, row4, row5]

    graph=Graph(maps)
    print(graph.kruskal())