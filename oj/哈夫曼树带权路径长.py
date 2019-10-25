"""
第一行输入一组正整数序列，元素之间以空格分开，以这组序列构造一颗huffman树，每个叶子结点的权值即为整数的值
输出以上huffman树的带权路径长度，树的带权路径长度规定为所有叶子结点的带权路径长度之和，记为WPL。
"""
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insert(list):
    h=[Node(i) for i in list]
    while len(h)!=1:
        h.sort(key=lambda node:node.val)        #对节点的val进行排序
        node=Node(h[0].val+h[1].val)            #最小的两个节点合并，并加入h
        node.left=h.pop(0)
        node.right=h.pop(0)
        h.append(node)
    return h[0]                                 #此时h只有一个元素（根节点）

def Wpl(root):                                  #规律：wpl等于每个非叶节点的节点权值之和
    if root.left and root.right:
        return root.val+Wpl(root.left)+Wpl(root.right)      #有左、右节点，说明不是叶节点，向下遍历
    else:
        return 0                                            #到底，返回0

if __name__ == '__main__':
    root=None
    depth=0
    list=input().split()
    list=[int(i) for i in list]
    root=insert(list)
    print(Wpl(root))



