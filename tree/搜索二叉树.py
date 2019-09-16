class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def insert(self,root,val):
        if root is None:
            root=Node(val)
        elif val>root.val:
            root.right=self.insert(root.right,val)
        elif val<root.val:
            root.left=self.insert(root.left,val)
        return root

    def query(self,root,val):
        if root is None:
            return False
        elif root.val==val:
            return True
        elif val>root.val:
            return self.query(root.right,val)
        elif val<root.val:
            return self.query(root.left,val)

    def findmin(self,root):
        if root.left:
            return self.findmin(root.left)
        else:
            return root

    def findmax(self,root):
        if root.right:
            return self.findmax(root.right)
        else:
            return root

    def delete(self,root,val):
        if root is None:
            return
        if val>root.val:
            root.right=self.delete(root.right,val)
        elif val<root.val:
            root.left=self.delete(root.left,val)
        else:
            if root.left is None and root.right is None:
                root=None
            elif root.left and root.right:
                temp=self.findmin(root.right)
                root.val=temp.val
                root.right=self.delete(root.right,temp.val)
            elif root.left is None:
                root=root.left
            else:
                root=root.right
        return root

    def printtree(self,root):
        if root is None:
            return
        self.printtree(root.left)
        print(root.val,end=' ')
        self.printtree(root.right)

if __name__ == '__main__':
    list=[12,53,767,134,6]
    root=None
    bst=BST()
    for i in list:
        root=bst.insert(root,i)
    print('max value: ', bst.findmax(root).val)
    print('min value: ', bst.findmin(root).val)
    print('search 12: ', bst.query(root, 12))
    print('max value: ', bst.findmax(root).val)
    print('min value: ', bst.findmin(root).val)
    bst.delete(root, 134)
    bst.printtree(root)

