class HashTable:
    def __init__(self):
        self.size=11                 #哈希表的长度
        self.slots=[None]*self.size
        self.data=[None]*self.size

    def hash(self,key):              #除留余数法确定键值的位置
        return key%len(self.slots)

    def rehash(self,key):            #再哈希
        return (key+1)%len(self.slots)

    def put(self,key,data):
        value=self.hash(key)
        if self.slots[value] is None:      #槽为空时，直接赋值
            self.slots[value]=key
            self.data[value]=data
        else:
            if self.slots[value]==key:
                data[value]=data          #匹配到键值，覆盖旧数据（哈希表长度有限）
            next_value=self.rehash(value)
            while self.slots[next_value] is not None and self.slots[next_value]!=key:     #若slots[next_value]非空且不匹配key，则不断再哈希
                next_value=self.rehash(next_value)
            if self.slots[next_value] is None:
                self.slots[next_value] = key
                self.data[next_value] = data
            else:
                self.data[next_value]=data

    def get(self,key):
        start=self.hash(key)
        data=None
        pos=start

        while self.slots[pos] is not None:
            if self.slots[pos]==key:
                data=self.data[key]
                break
            else:
                pos=self.rehash(pos)
                if pos==start:
                    break                       #再哈希等于自身，将无限循环，此时将其退出
        return data

    def __getitem__(self, item):                #重写[]，直接通过[]而不是调用函数来执行get
        return self.get(item)

    def __setitem__(self, key, value):          #重写[]的赋值
        self.put(key,value)

if __name__=='__main__':
    h=HashTable()
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[85] = 'bee'
    h[34] = 'fish'

    print(h.slots)
    print(h.data)
