"""
input:输入一组数据，该数据为纯数字组合，数据与数据间以空格分开，数据末尾没有空格。
ouput:输出共有两行，第一行该红黑树的前序遍历结果，不需换行，每个数据间留一个空格；
	  第二行输出对应节点的颜色，红色代表0，黑色代表1，不需换行，每个数据间留一个空格.
"""
class Node:
	def __init__(self,val):
		self.val=val
		self.color='B'
		self.left=None
		self.right=None
		self.father=None
		self.size=None

class RedBlckTree:
	def __init__(self):
		self.nil=Node(None)        #尾节点
		self.root=self.nil         #根节点

def left_rotation(tree,node):
	right=node.right
	node.right = right.left             #第一步，移动左节点
	if right.left!=tree.nil:
		right.left.father=node


	right.father=node.father            #第二步，设置父节点
	if node.father==tree.nil:
		tree.root=right
	elif node==node.father.left:
		node.father.left=right
	else:
		node.father.right=right

	right.left=node                     #第三步，左旋
	node.father=right

def right_rotation(tree,node):
	left=node.left
	node.left=left.right
	if left.right!=tree.nil:
		left.right.father=node
	left.father=node.father
	if node.father==tree.nil:
		tree.root=left
	elif node==node.father.right:
		node.father.right=left
	else:
		node.father.left=left
	left.right=node
	node.father=left

def insert(tree,val):
	node=Node(val)
	r=tree.nil
	temp=tree.root
	while temp!=tree.nil:       #向下找到待插入节点的父节点
		r=temp
		if val>temp.val:
			temp=temp.right
		else:
			temp=temp.left
	node.father=r
	if r==tree.nil:             #比较和父节点的大小，判断插入的位置(左右)
		tree.root=node
	elif val>r.val:
		r.right=node
	else:
		r.left=node

	node.left=tree.nil          #插入后的节点指向节点nil
	node.right=tree.nil
	node.color='R'
	rb_fixup(tree,node)

def rb_fixup(tree,node):
	while node.father.color=='R':
		if node.father==node.father.father.left:
			uncle=node.father.father.right
			if uncle.color == 'R':              #叔父节点为红，分别涂色
				uncle.color='B'
				node.father.color='B'
				node.father.father.color='R'
				node=node.father.father         #node变为爷节点重复while
			else:                               #无叔父节点或其颜色为黑，旋转且涂色
				if node==node.father.right:
					node=node.father
					left_rotation(tree,node)
				node.father.color='B'
				node.father.father.color='R'
				right_rotation(tree,node.father.father)   #右旋完成后，node变为爷节点

		else:
			uncle=node.father.father.left
			if uncle.color=='R':
				uncle.color='B'
				node.father.color='B'
				node.father.father.color='R'
				node=node.father.father
			else:
				if node==node.father.left:
					node=node.father
					right_rotation(tree,node)
				node.father.color='B'
				node.father.father.color='R'
				left_rotation(tree,node.father.father)
	tree.root.color='B'

def pre_traversal(root):            #前序遍历
	if root is None:
		return
	if root.val:
		print(root.val,end=' ')
	pre_traversal(root.left)
	pre_traversal(root.right)

def print_color(root):
	if root is None:
		return
	if root.val:                #排除nil节点的情况
		if root.color == 'R':
			print(0, end=' ')
		else:
			print(1, end=' ')
	print_color(root.left)
	print_color(root.right)

if __name__ == '__main__':
    RBtree=RedBlckTree()
    list=map(int,input().split())
    for i in list:
        insert(RBtree,i)
    pre_traversal(RBtree.root)
    print('')
    print_color(RBtree.root)