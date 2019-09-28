class Queue:               #用于层次遍历
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0

    def isEmpty(self):
        return self.head == self.tail
    def push(self,data):
        self.data.append(data)
        self.tail = self.tail + 1
    def pop(self):
        temp = self.data[self.head]
        self.head = self.head + 1
        return temp
    def count(self):
        return self.tail - self.head
    def print(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

    def getdata(self):
        return self.data
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def getheight(self):
        return self.height
    def setdata(self,data):
        self.data = data
        return
    def setleft(self,left):
        self.left = left
        return
    def setright(self,right):
        self.right=right
        return
    def setheight(self,height):
        self.height=height
        return

def getheight(node):
    if node is None:
        return 0
    return node.getheight()

def max(a,b):
    return a if a>b else b

def leftrotation(node):
    ret=node.getleft()
    node.setleft(ret.getright())
    ret.setright(node)
    h1=max(getheight(node.getleft()),getheight(node.getright()))+1
    node.setheight(h1)
    h2=max(getheight(ret.getleft()),getheight(ret.getright()))+1
    ret.setheight(h2)
    return ret

def rightrotation(node):
    ret=node.getright()
    node.setright(ret.getleft())
    ret.setleft(node)
    h1=max(getheight(node.getleft()),getheight(node.getright()))+1
    node.setheight(h1)
    h2=max(getheight(ret.getleft()),getheight(ret.getright()))+1
    ret.setheight(h2)
    return ret

def rlrotation(node):                                    #子树左旋，根右旋
    node.setleft(rightrotation(node.getleft()))
    return leftrotation(node)

def lrrotation(node):
    node.setright(leftrotation(node.getright()))
    return rightrotation(node)


def insert(node,data):
    if node is None:
        return Node(data)
    if data < node.getdata():
        node.setleft(insert(node.getleft(),data))
        if getheight(node.getleft())-getheight(node.getright())==2:
            if data<node.getleft().getdata():                         #通过和根节点的左右子节点比较大小，得出新节点在左(右)子节点的左部分还是右部分
                node=leftrotation(node)
            else:
                node=rlrotation(node)
                r"""
                第一种情况：图2，F在B的左部分，直接右旋即可，第二种情况，图1，F在B右部分，执行rl
                A              A                                   
               / \            / \                  
              B   C          B   C               
             / \            /     \                          
            D   E          D       E             
                 \        /
                  F      F

                """
    else:
        node.setright(insert(node.getright(),data))
        if getheight(node.getright())-getheight(node.getleft())==2:
            if data<node.getright().getdata():
                node=lrrotation(node)
            else:
                node=rightrotation(node)

    h=max(getheight(node.getleft()),getheight(node.getright()))+1
    node.setheight(h)
    return node

def getmin(node):
    while node.getleft() is not None:
        node=node.getleft()
    return node.getdata()

def delete(node,data):
    if data==node.getdata():
        if node.getleft() is not None and node.getright() is not None:         #这组if-else用于删除相应节点，并保持搜索二叉树的特点，但未必平衡
            temp=getmin(node.getright())
            node.setdata(temp)
            node.setright(delete(node.getright(),temp))
        elif node.getleft() is not None:
            node=node.getleft()
        else:
            node=node.getright()
    elif data>node.getdata():
        if node.getright() is None:
            return node
        else:
            node.setright(delete(node.getright(),data))
    else:
        if node.getleft() is None:
            return node
        else:
            node.setleft(delete(node.getleft(),data))

    if node is None:                                                       #这组if-else用于维持二叉树平衡，原理和insert相同
        return node
    elif getheight(node.getleft())-getheight(node.getright())==2:
        if getheight(node.getleft().getleft())>getheight(node.getleft().getright()):
            node=leftrotation(node)
        else:
            node=rlrotation(node)
    elif getheight(node.getleft())-getheight(node.getright())==-2:
        if getheight(node.getright().getleft())>getheight(node.getright().getright()):
            node=lrrotation(node)
        else:
            node=rightrotation(node)

    h=max(getheight(node.getleft()),getheight(node.getright()))+1
    node.setheight(h)
    return node

class AVLtree:
    def __init__(self):
        self.root=None

    def length(self):
        return getheight(self.root)
    def isempty(self):
        return self.length()==0
    def insert(self,data):
        self.root=insert(self.root,data)
    def delete(self,data):
        if self.root is None:
            print('Empty tree')
        else:
            self.root=delete(self.root,data)

    def traversal(self):     #层次遍历,以树状输出
        q = Queue()
        q.push(self.root)
        layer = self.length()
        if layer == 0:
            return
        cnt = 0
        while not q.isEmpty():
            node = q.pop()
            space = " " * int(pow(2, layer - 1))
            print(space, end="")
            if node is None:
                print("*", end="")
                q.push(None)
                q.push(None)
            else:
                print(node.getdata(), end="")
                q.push(node.getleft())
                q.push(node.getright())
            print(space, end="")
            cnt = cnt + 1
            for i in range(100):
                if cnt == pow(2, i) - 1:
                    layer = layer - 1
                    if layer == 0:
                        print()
                        print("*************************************")
                        return
                    print()
                    break
        print()
        print("*************************************")
        return

if __name__ == "__main__":
    t = AVLtree()
    list=[144,32,6,78,45,43]
    for i in list:
        t.insert(i)
    t.traversal()

    t.insert(2)
    t.insert(1)
    t.traversal()

    t.delete(144)
    t.traversal()





