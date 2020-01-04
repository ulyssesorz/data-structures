class Node:
    def __init__(self,value):
        self.value=value
        self.pre=None
        self.next=None

class Linklist2:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None

    def insert_head(self,value):
        node=Node(value)
        if self.is_empty():
            self.head=Node(value)
        else:
            node.next=self.head
            self.head.pre=node
            self.head=node

    def insert_tail(self,value):
        node=Node(value)
        if self.is_empty():
            self.head=node
            return
        cur=self.head
        while cur.next:             #移动到末端
            cur=cur.next
        node.pre=cur
        cur.next=node

    def insert(self,pos,value):     #插入到第pos个元素后面
        if pos<=0:
            self.insert_head(value)
        elif pos>len(self)-1:
            self.insert_tail(value)
        else:                       #插入到中间指定位置
            node=Node(value)
            cur=self.head
            count=0
            while count<pos-1:
                cur=cur.next
                count+=1
            node.next=cur.next
            cur.next.pre=node
            node.pre=cur
            cur.next=node

    def search(self,value):
        cur=self.head
        while cur:
            if cur.value==value:
                return True
            else:
                cur=cur.next
        return False

    def delete(self,value):
        if self.is_empty():
            return
        cur=self.head
        while cur:
            if cur.value==value:
                if cur==self.head:
                    self.head=cur.next
                    if cur.next:
                        cur.next.pre=None
                else:
                    cur.pre.next=cur.next
                    if cur.next:
                        cur.next.pre=cur.pre
            else:
                cur=cur.next

    def print_list(self):               #反向输出
        cur=self.head
        while cur.next:
            cur=cur.next
        while cur:
            print(cur.value,end=' ')
            cur=cur.pre

if __name__ == '__main__':
    ll=Linklist2()
    li=[1,4,6,24,7,13,8,36,120]
    for i in li:
        ll.insert_head(i)
    ll.print_list()