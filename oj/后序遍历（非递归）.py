"""
二叉树后序遍历的非递归实现，使用两个栈实现
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

    def mid_traversal(self):                #将头结点压入stack1，stack1弹出一个节点，然后依次将其左节点和右节点压入stack1
        stack1=[]                           #重复上述步骤，并且每次将stack1弹出的节点压入stack2中（为了倒叙输出）
        stack2=[]
        stack1.append(self.root)
        while stack1:
            current=stack1.pop()
            stack2.append(current)
            if current.lchild is not None:      #None不输出
                if current.lchild.elem is None:
                    pass
                else:
                    stack1.append(current.lchild)
            if current.rchild is not None:
                if current.rchild.elem is None:
                    pass
                else:
                    stack1.append(current.rchild)
        for i in range(len(stack2)):
            print(stack2.pop().elem)


if __name__ == '__main__':

    tree=MyTree()
    list=input().split()

    if list[0]!='#':
        for i in list:
            tree.insert(i)
        tree.mid_traversal()
