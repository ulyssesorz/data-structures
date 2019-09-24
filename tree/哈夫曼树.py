class Node:
    def __init__(self,name=None,value=None):
        self.name=name
        self.value=value
        self.left=None
        self.right=None

class HuffmanTree:
    def __init__(self,char_weight):
        self.a=[Node(part[0],part[1]) for part in char_weight]
        while len(self.a)!=1:
            self.a.sort(key=lambda node:node.value,reverse=True)
            c=Node(value=self.a[-1].value+self.a[-2].value)
            c.left=self.a.pop()
            c.right=self.a.pop()
            self.a.append(c)                                        #完成后a内不再是列表，而是一个树(只有一个根节点)在a里面
        self.root=self.a[0]
        self.b=[0]*10

    def pre(self,tree,length):
        node=tree
        if not node:                            #遍历到叶节点之后则返回
            return
        elif node.name:                         #遍历到叶节点，停下来打印存在b中的编码
            print(node.name,':',end=' ')
            for i in range(length):
                print(self.b[i],end=' ')
            print(' ')
            return

        self.b[length]=0                        #往左遍历，左子树的边赋0，直到叶节点
        self.pre(node.left,length+1)
        self.b[length]=1                        #往右遍历，右子树的边赋1，直到叶节点
        self.pre(node.right,length+1)

    def get_code(self):
        self.pre(self.root,0)


if __name__=='__main__':
    char_weights = [('a', 9), ('b', 12), ('c', 6), ('d', 3), ('e', 5), ('f', 15)]
    tree = HuffmanTree(char_weights)
    tree.get_code()

