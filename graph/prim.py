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

    def prim(self):
        """
        解决图的最小生成树问题，原理是“找点”
        """
        res=[]
        if self.node_num<0 or self.edge_num<self.node_num-1:
            return res
        selected_node=[0]         #第一个节点
        candidate_node=[i for i in range(1,self.node_num)]    #剩下的节点

        while len(candidate_node)!=0:
            begin,end,min=0,0,9999
            for i in selected_node:
                for j in candidate_node:
                    if self.graph[i][j]<min:     #对于选定的点i，检查与其连通的j，找出最小的i-j距离
                        begin=i
                        end=j
                        min=self.graph[i][j]
            res.append([begin,end,min])         #存入父节点、子节点以及他们的距离
            selected_node.append(end)           #将刚刚选择的子节点放入待定的父节点列表中，原父节点不可删除，他可能再次成为父节点
                                                #子节点被加入到selected中，以后就不可能再成为子节点（被连接第二次）了，避免形成回路
            candidate_node.remove(end)
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
    print(graph.prim())