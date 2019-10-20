"""
按照层次遍历给出一颗二叉搜索树，例如：3 1 4 # # 2 #，以空格分开，其中#号代表对应的节点处为空
"""
class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

def level_insert(root,val):        #按照题目所给还原该树
    if root is None:               #空树，生成根节点
        root=Node(val)
    else:                               #层次遍历的思想，利用队列
        queue=[]
        queue.append(root)
        while queue:
            current=queue.pop(0)
            if current.left is None:
                if val=='#':
                    current.left = Node(None)
                else:
                    current.left = Node(val)
                break                           #插入后break，否则同层其他左节点也会被插入data
            elif current.right is None:
                if val == '#':
                    current.right = Node(None)
                else:
                    current.right = Node(val)
                break
            else:
                queue.append(current.left)
                queue.append(current.right)
    return root

def isBst(root,min,max):
    if root is None or root.val is None:            #遍历到叶节点还未出现矛盾，返回True
        return True
    if int(root.val)<min or int(root.val)>max:
        return False
    return isBst(root.left,min,int(root.val)-1) and isBst(root.right,int(root.val)+1,max)  #递归地比较每一个节点，注意最大、小值的变化
                                                                                           #确保每个左节点不大于父节点，每个右节点不小于父节点

if __name__=='__main__':
    list=input().split()
    root=None
    for i in list:
        root=level_insert(root,i)
    list=[int(i) for i in list if i!='#']       #除去#
    max_val=max(list)+1
    min_val=min(list)-1
    if isBst(root,min_val,max_val):
        print('True')
    else:
        print('False')







