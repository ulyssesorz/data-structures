class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def display(tree):
    if tree is None:
        return
    if tree.left is not None:
        display(tree.left)
    print(tree.data)
    if tree.right is not None:
        display(tree.right)
    return

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


def main(): # Main func for testing.
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)

    print(isfull(tree))
    print(depth(tree))
    print("Tree is: ")
    display(tree)


if __name__ == '__main__':
    main()