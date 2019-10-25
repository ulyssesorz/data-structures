"""
给定一个二叉树返回所有大于等于 L 小于等于R的节点的值的和。二叉搜索树保证具有唯一的值。-1代表空节点。
第一行是一个数组，代表了二叉搜索树。第二行分别是L和R。
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

def plus(root,min,max):
    if root is None:                #到叶节点结束
        return 0
    if root.val<=max and root.val>=min:                 #遍历每个节点，若满足则加上val，不满足则跳过该节点，遍历其子节点
        return plus(root.left,min,max)+plus(root.right,min,max)+root.val
    else:
        return plus(root.left,min,max)+plus(root.right,min,max)

if __name__ == '__main__':
    root=None
    list=input().split()
    list=[int(i) for i in list]
    for i in list:
        root = insert(root, i)
    list2 = input().split()
    list2 = [int(i) for i in list2]
    if list[0]==-1:
        print(0)
    else:
        print(plus(root, list2[0], list2[1]))