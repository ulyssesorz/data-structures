"""
判断一棵树是否是二叉搜索树的第二种解法：若是二叉搜索树，其中序遍历就是升序排列
因此，用isbst得出其中序遍历的结果，再和sorted后的结果比较即可
"""
class Node:
	def __init__(self,val):
		self.val=val
		self.left=None
		self.right=None
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

def isBst(root,result):
	if root is None:
		return
	isBst(root.left,result)         #类比中序遍历，将输出改为加到result中
	result.append(root.val)
	isBst(root.right,result)

if __name__ == '__main__':
	list = input().split()
	root = None
	for i in list:
		root = level_insert(root, i)
	list = [int(i) for i in list if i != '#']  # 除去#
	list=sorted(list)           #得到升序排列
	result=[]
	isBst(root,result)
	result=[int(i) for i in result if i!=None]  #除去None
	if list==result:
		print('True')
	else:
		print('False')