class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None

    def insert_head(self,data):
        newnode=Node(data)
        if self.head!=None:
            newnode.next=self.head
        self.head=newnode

    def insert_tail(self,data):
        if self.head == None:
            self.insert_head(data)
        else:
            tmp=self.head
            while tmp.next != None:
                tmp=tmp.next
            tmp.next=Node(data)

    def insert(self,index,data):
        tmp=self.head
        if index>self.getlength():
            print('error')
        elif index==1:
            self.insert_head(data)
        elif index==self.getlength():
            self.insert_tail(data)
        else:
            for i in range(1,index-1):             #定位到index的前一个节点
                tmp=tmp.next
            newnode=Node(data)
            newnode.next=tmp.next
            tmp.next = newnode

    def getlength(self):
        tmp=self.head
        count=1
        if tmp is None:
            return 0
        while tmp.next!=None:
            tmp=tmp.next
            count+=1
        return count

    def search(self,data):
        tmp=self.head
        count=0
        while tmp:
            count+=1
            if tmp.data==data:
                return count
            else:
                tmp=tmp.next


    def delete(self,data):
        tmp=self.head
        if tmp.data==data:
            self.head=self.head.next
        while tmp.next:
            if tmp.next.data==data:
                tmp.next=tmp.next.next         #删除下一个节点的方法
            else:
                tmp=tmp.next

    def reverse(self):               #链表的反转
        temp=None
        current=self.head

        while current:
            nextnode=current.next
            current.next=temp        #current往回指

            temp=current             #temp和current往后移准备下一次反转
            current=nextnode
        self.head=temp
    def printlist(self):
        tmp=self.head
        while tmp:
            print(tmp.data)
            tmp=tmp.next

    def isempty(self):
        return self.head==None

if __name__ == '__main__':
    A=Linked_List()
    a1=input('Insert1>>')
    a2=input('Insert2>>')
    a3=input('Insert3>>')
    A.insert_head(a1)
    A.insert_tail(a2)
    A.insert_tail(a3)
                                       #test: a1,a2,a3=1,2,3
    print(A.search(a2))

    A.insert(2,77)
    A.printlist()

    A.delete(a2)
    A.printlist()

    A.reverse()
    A.printlist()
