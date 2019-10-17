"""
通过中序遍历和后序遍历确定前序遍历
"""
class Node:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right

def struct_tree(mid,post):              #类比上题
    if len(post)==0:
        return None
    root=post[len(post)-1]
    i=mid.index(root)
    left=struct_tree(mid[0:i],post[0:i])
    right=struct_tree(mid[i+1:],post[i:len(post)-1])
    return Node(root,left,right)

def pre_traversal(root):              #前序遍历
    if root is None:
        return
    else:
        print(root.data,end=' ')
        pre_traversal(root.left)
        pre_traversal(root.right)

if __name__=='__main__':
    list1=input().split()
    list2=input().split()

    root=struct_tree(list1,list2)
    pre_traversal(root)