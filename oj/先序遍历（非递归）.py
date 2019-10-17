"""
二叉树先序遍历的非递归实现，使用栈
空节点#不用输出
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

    def pre_traversal(self):
        stack=[]                    #建栈，压入父节点，输出父节点，压入右节点，压入左节点，重复上述步骤
        stack.append(self.root)
        while stack:
            cur=stack.pop()
            if cur.elem is None:        #空节点无子节点，不输出
                pass
            else:
                print(cur.elem)
            if cur.rchild is not None:
                stack.append(cur.rchild)
            if cur.lchild is not None:
                stack.append(cur.lchild)

if __name__ == '__main__':

    tree=MyTree()
    list=input().split()

    if list[0]!='#':
        for i in list:
            tree.insert(i)
        tree.pre_traversal()









