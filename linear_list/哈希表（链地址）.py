class HashTable:
    """
    第一行数字表示要建立的散列表的大小，第二行表示要作为元素建立散列表的整数序列（
    注意：元素之间以空格分开，第一行散列表大小并不表示本行元素的数量），
    第三行表示要插入元素的数量n，接下来n行表示待插入元素值；下一行表示要删除元素的数量m，
    接下来m行表示待删除元素值；下一行表示要查找元素的数量r，接下来r行表示待查找元素值。
    """
    def __init__(self, size):
        self.size = size
        self.slots = [[] for i in range(self.size)]         #哈希表的每一项是列表，可放置冲突的值

    def hash(self,key):
        return key%len(self.slots)                          #除留余数法确定键值的位置

    def linkhash(self,key,data):                            #链地址法解决冲突
        if data in self.slots[key]:                         #避免重复
            return
        self.slots[key].append(data)

    def insert(self,data):
        value=self.hash(data)
        self.linkhash(value,data)

    def delete(self,data):
        value=self.hash(data)                  #通过哈希函数映射到slots中
        if data in self.slots[value]:
            self.slots[value].remove(data)
            return
        print('Delete Error')


    def search(self,data):
        value = self.hash(data)
        if data in self.slots[value]:
            print('True')
            return
        print('False')

if __name__=='__main__':

    length=int(input())                 #建立哈希表
    h=HashTable(length)

    list=input().split()            #读取并插入序列
    list=[int(i) for i in list]
    for i in range(len(list)):
        h.insert(list[i])

    n=int(input())                 #插入
    for i in range(n):
        h.insert(int(input()))

    m=int(input())                  #删除
    for j in range(m):
        h.delete(int(input()))

    r=int(input())                  #查找
    for i in range(r):
        h.search(int(input()))



