class Stack:

    def __init__(self):
        self.item=[]

    def push(self,data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def clear(self):
        del self.item[:]

    def size(self):
        return len(self.item)

    def isempty(self):
        return self.size()==0

    def top(self):                        #返回栈顶的元素，但不删除
        return self.item[self.size()-1]

if __name__ == '__main__':

    A=Stack()
    for i in range(1,5):
        A.push(i)

    print(A.top())

    if not A.isempty():
        print(A.size())

    for i in range(1, 5):
        print(A.pop())

    A.clear()
    print(A.isempty())