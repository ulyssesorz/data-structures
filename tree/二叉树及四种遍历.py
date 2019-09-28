class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isfull(tree):
    if tree is None:
        return True
    if tree.left is None and tree.right is None:
        return True
    if tree.left is not None and tree.right is not None:
        return isfull(tree.left) and isfull(tree.right)
    else:
        return False

def depth(tree):
    if tree is None:
        return 0
    else:
        depthleft=depth(tree.left)+1
        depthright=depth(tree.right)+1
        if depthleft>depthright:
            return depthleft
        else:
            return depthright

def pre_traversal(root):              #前序遍历
    if root is None:
        return
    else:
        print(root.data,end=' ')
        pre_traversal(root.left)
        pre_traversal(root.right)

def mid_traversal(root):             #中序遍历
    if root is None:
        return
    else:
        mid_traversal(root.left)
        print(root.data, end=' ')
        mid_traversal(root.right)

def post_traversal(root):           #后序遍历
    if root is None:
        return
    else:
        post_traversal(root.left)
        post_traversal(root.right)
        print(root.data, end=' ')

def level_traversal(root):          #层次遍历
    if root is None:
        return
    q=[]
    q.append(root)
    while q:
        current=q.pop(0)
        print(current.data,end=' ')
        if current.left is not None:
            q.append(current.left)
        if current.right is not None:
            q.append(current.right)


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.left.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)

    print(isfull(tree))
    print(depth(tree))
    print("Tree is: ")
    pre_traverse(tree)
    print('\n')
    mid_traverse(tree)
    print('\n')
    post_traverse(tree)
    print('\n')
    level_traverse(tree)
