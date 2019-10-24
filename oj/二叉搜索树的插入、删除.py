"""
input:第一行的输入为一组数据，以空格分开，由数字构成，数据不会重复，根据这个序列可以构造出唯一的一颗二叉搜索树；
      第二行表示待插入元素的数量n，接下来的n行每行均为一个待插入元素值；
      接下来的一行输入为一个数字m，接下来m行每行均为一个需要删除的数据。
putput:插入数据之后需要对二叉树进行一次先序遍历；
       删除数据时，若删除成功则进行一次后序遍历，若删除失败（即不存在该节点），则输出‘Delete Error’，并且不进行后序遍历。
       PS：遍历输出节点时使用print(a,end=’ ’)语句，每次遍历之后都需换行。
"""
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insert(root,val):
    if root is None:                        #遍历到叶节点时插入新节点
        root=Node(val)
    elif val>root.val:
        root.right=insert(root.right,val)
    else:
        root.left=insert(root.left,val)
    return root

def findmin(root):                      #递归地找到最小的节点，用于删除操作
    if root.left:
        return findmin(root.left)
    else:
        return root

def delete(root,val):                   #原理类似insert，递归地比较节点大小，找到要删除的节点
    if root is None:
        return
    if val>root.val:
        root.right=delete(root.right,val)
    elif val<root.val:
        root.left=delete(root.left,val)
    else:
        if root.left is None and root.right is None:       #叶节点，直接删除即可
            root=None
        elif root.left is None:                            #让子节点代替父节点
            root=root.right
        elif root.right is None:
            root=root.left
        else:
            temp=findmin(root.right)                        #将该节点的值改为右子树的最小值，再删除最小值的节点
            root.val=temp.val                               #相当于用最小值节点代替了该节点
            root.right=delete(root.right,temp.val)
    return root

def query(root,val):                                        #查找val是否在树中
    if root is None:
        return False
    elif root.val==val:
        return True
    elif root.val>val:
        return query(root.left,val)
    else:
        return query(root.right,val)


def pre_traversal(root):        #前序遍历
    if root is None:
        return
    print(root.val,end=' ')
    pre_traversal(root.left)
    pre_traversal(root.right)

def post_traversal(root):       #后序遍历
    if root is None:
        return
    post_traversal(root.left)
    post_traversal(root.right)
    print(root.val,end=' ')

if __name__ == '__main__':
    root=None
    list=input().split()
    list=[int(i) for i in list]
    for i in list:
        root=insert(root,i)
    n=int(input())
    for i in range(n):          #插入操作
        num=int(input())
        root=insert(root,num)
        pre_traversal(root)
        print('')
    m=int(input())
    for i in range(m):          #删除操作
        num=int(input())
        if query(root,num):
            root=delete(root,num)
            post_traversal(root)
            print('')
        else:
            print('Delete Error')