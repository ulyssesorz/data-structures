"""
通过前序遍历和中序遍历确定后序遍历
利用“前序遍历的第一个节点是根节点”这一性质，递归地建立节点
"""
class Node:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right

def struct_tree(pre,mid):
    if len(pre)==0:
        return None
    root=pre[0]                 #pre的第一个节点就是该（子）树的根节点
    i=mid.index(root)
    left=struct_tree(pre[1:i+1],mid[:i])
    right=struct_tree(pre[i+1:],mid[i+1:])  #递归对每个子树进行建树
    return Node(root,left,right)

def post_traversal(root):           #后序遍历
    if root is None:
        return
    else:
        post_traversal(root.left)
        post_traversal(root.right)
        print(root.data, end=' ')

if __name__=='__main__':
    list1=input().split()
    list2=input().split()

    root=struct_tree(list1,list2)
    post_traversal(root)