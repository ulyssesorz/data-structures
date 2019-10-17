"""
构造完全二叉树，并实现访问操作
"""
class Node:
    def __init__(self,elem):
        self.elem=elem
        self.lchild=None
        self.rchild=None

class MyTree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:               #空树，生成根节点
            self.root=Node(data)
        else:                               #层次遍历的思想，利用队列
            queue=[]
            queue.append(self.root)
            while queue:
                current=queue.pop(0)
                if current.lchild is None:
                    if data=='#':
                        current.lchild=Node(None)
                    else:
                        current.lchild = Node(data)
                    break                           #插入后break，否则同层其他左节点也会被插入data
                elif current.rchild is None:
                    if data=='#':
                        current.rchild=Node(None)
                    else:
                        current.rchild = Node(data)
                    break
                else:
                    queue.append(current.lchild)
                    queue.append(current.rchild)

if __name__ == '__main__':
    MyTree=MyTree()
    list=input().split()

    if list ==[]:             #输入空树（回车）时，输出None
        temp=input()          #骗oj...可忽略
        print(None)
    else:
        for i in list:
            MyTree.insert(i)
        N=int(input())
        for i in range(N):
            eval(input())

# e.g. print(MyTree.root.rchild.lchild.elem)
#      print(MyTree.root.lchild.lchild.elem)






