"""
给定一组输入数据，要求判断这组输入数据构成的二叉树是否是AVL树。
PS：所谓AVL树是指它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且其左右子树也都是一棵AVL树。
PS:AVL树既是平衡树也是二叉搜索树。
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

def getheight(root):
    if root is None or root.val is None:                      #遍历到叶节点返回-1（因为边数是点数-1）
        return -1
    else:
        rheight=getheight(root.right)
        lheight=getheight(root.left)
        return rheight+1 if rheight>lheight else lheight+1      #返回大的长度

def isAVL(root):
    if root is None or root.val is None:
        return True
    lheight=getheight(root.left)
    rheight=getheight(root.right)
    h=abs(lheight-rheight)                                      #长度差值
    return h<=1 and isAVL(root.left) and isAVL(root.right)

def isBst(root,min,max):
    if root is None or root.val is None:                        #是avl的前提是它是一个二叉搜索树
        return True
    if int(root.val)<min or int(root.val)>max:
        return False
    return isBst(root.left,min,int(root.val)-1) and isBst(root.right,int(root.val)+1,max)


if __name__=='__main__':
    list=input().split()
    root=None
    for i in list:
        root=level_insert(root,i)
    list = [int(i) for i in list if i != '#']       # 除去#
    if list==[]:                                    # 空树
        print('True')
    else:
        max_val = max(list) + 1
        min_val = min(list) - 1
        if isAVL(root) and isBst(root, min_val, max_val):
            print('True')
        else:
            print('False')








