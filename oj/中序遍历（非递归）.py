"""
二叉树中序遍历的非递归实现，使用栈实现
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

    def post_traversal(self):
        stack=[]
        cur=self.root
        while stack or cur is not None:
            if cur is not None:            #向左遍历，把左节点都压入stack中
                stack.append(cur)
                cur = cur.lchild
            else:                          #遍历到叶节点，输出（最左端的叶节点）
                cur=stack.pop()
                print(cur.elem)
                cur=cur.rchild             #检查cur的右节点能否向下遍历（执行上面的if）


if __name__ == '__main__':

    tree=MyTree()
    list=input().split()

    if list[0]!='#':
        for i in list:
            tree.insert(i)
        tree.post_traversal()
