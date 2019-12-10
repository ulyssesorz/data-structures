"""
input:第一行输入一个正整数t，表示要构造2t阶B树；第二行输入一个正整数n,
表示分别将1,2，…,n作为关键词按照顺序构造对应的B树。
output:第一行输出你构造的B树从上到下每一层的最左节点的第一个关键词（以空格分隔），
第二行输出你构造的B树从上到下每一层的最右节点的最后一个关键词（以空格分隔
"""
class Node(object):
	def __init__(self, data=[],child=[]):
		self.data = data            #数据域,存int型的值
		self.children = child       #children是列表，里面是多个节点类

class Tree(object):
	def __init__(self, data, nodes=[], degrees=2):
		self.root = Node([data])
		self.nodes = nodes
		self.degrees = degrees

	def insert(self, key):
		if len(self.root.data) == 2 * self.degrees - 1:       #插入已满节点
			r = self.root
			self.root = Node([],[r])
			self.splitChild(self.root, r)
			self.insertNonfull(self.root, key)
		else:                                                      #插入未满节点
			self.insertNonfull(self.root, key)

	def insertNonfull(self, root, key):
		if root.children == []:         #插入只能插入到叶节点中
			root.data.append(key)
			root.data.sort()
		else:                           #非叶节点，向下寻找要插入的子节点，并检查是否有满的节点需要分裂
			c = None
			for i in root.children:
				for j in i.data:
					if key < j:
						c = i           #找到key应该插入的节点c
						break
				c = root.children[-1]   #c默认大于所有子节点，若不执行break则放在最后一个子节点中

			if len(c.data) == 2 * self.degrees - 1:       #如果此时被插入的节点已满，需先分裂
				self.splitChild(root, c)
				for i in root.children:                 #再次寻找要插入的节点，此次不可能再满
					for j in i.data:
						if key < j:
							c = i
							break
					c = root.children[-1]
			self.insertNonfull(c, key)          #递归，直到找到叶节点

	def splitChild(self, node, child):     #节点分裂操作
		child1 = Node([])
		child2 = Node([])
		child1.data.extend(child.data[:len(child.data)//2])     #加入左半边数据域的值
		child2.data.extend(child.data[len(child.data)//2+1:])   #加入右半边数据域的值 （两次加入不包括中间值）
		if child.children:
			child1.children=child.children[:int((len(child.children) / 2))]
			child2.children=child.children[int((len(child.children) / 2)):]   #同上，平分children

		mid = child.data[len(child.data)//2]                   #得到中间值
		node.children.remove(child)         #移除需分裂的子节点
		li = []
		for i in node.children:
			li.append(i)                    #li内是不用分裂的其他子节点
		li.extend([child1, child2])         #加入分裂后形成的两个节点

		node.children=li
		node.data.append(mid)
		node.data.sort()

def traversal_left(node):               #向左遍历
	print(node.data[0],end=' ')         #输出数据域的第一个即最左侧的值
	if node.children==[]:
		return                          #到叶节点，返回
	else:
		traversal_left(node.children[0])

def traversal_right(node):              #同上
	print(node.data[-1],end=' ')
	if node.children==[]:
		return
	else:
		traversal_right(node.children[-1])

if __name__ == '__main__':
	m=int(input())
	n=int(input())
	tree = Tree(1,[],m)     #建树
	for i in range(2, n+1):
		tree.insert(i)      #插入后面的值

	traversal_left(tree.root)
	print( )
	traversal_right(tree.root)