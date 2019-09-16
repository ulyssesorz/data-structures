class Queue:
    def __init__(self):
        self.item=[]

    def enqueue(self,data):
        self.item.append(data)

    def dequeue(self):         #python中队列的实现和栈几乎一致，区别在于pop的方向
        return self.item.pop(0)

    def size(self):
        return len(self.item)

    def isempty(self):
        return self.size()==0

if __name__== '__main__':

    A=Queue()
    for i in range(1, 5):
        A.enqueue(i)

    print(A.size())
    print(A.dequeue())

"""
另一种python自带的方法
import queue

A=queue.Queue()
for i in range(5):
    A.put(i)
while not A.empty():
    print(A.get())
"""
