"""
第一行输入一个数n，(1<=n<=20)表示有n个序列需要判断；
接下去一行是一个初始序列，序列长度小于等于10，包含(0~9)的数字，没有重复数字，根据这个序列可以构造出唯一的一颗二叉搜索树；
再接下去的n行有n个序列，每个序列格式跟第一个序列一样，请判断每个序列是否与第一个序列表示同一颗二叉搜索树。

比较方式是 递归地比较每一个非None节点
"""
class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val


def insert(root,val):
    if root is None:
        root=Node(val)
    elif val>root.val:
        root.right=insert(root.right,val)
    elif val<root.val:
        root.left=insert(root.left,val)
    return root

def compare(root1,root2):
    if root1 is None and root2 is None:         #排除到底部的情况
        return True
    if root1 is None and roo2 is not None:
        return False
    if root1 is not None and root2 is None:     #这两个if是判断不同的条件，只要出现一个false就退出函数
        return False
    if root1.val==root2.val:                    #相等则递归地compare子节点
        return compare(root1.left,root2.left) and compare(root1.right,root2.right)


if __name__=='__main__':
    n=int(input())

    init=input()
    root=None
    for i in init:
        root=insert(root,i)         #得到初始序列的根节点
    r=[]                            #存放待比较树的根节点
    root2=None
    for i in range(n):
        list=input()
        for j in list:
            root2=insert(root2,j)
        r.append(root2)
        root2=None                  #存完一个节点记得“置零”

    for i in range(n):
        if compare(root,r[i]):
            print('YES')
        else:
            print('NO')




