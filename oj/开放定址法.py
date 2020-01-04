def add(table,data):
    for i in data:
        index=i%len(table)
        if table[index] is not None:
            j=0
            while table[(index+j)%len(table)] is not None:
                j+=1
            table[(index+j)%len(table)]=i
        else:
            table[index]=i
    return table

def search(table,num):
    if num not in table:
        return -1
    index=num%len(table)
    count=1
    if table[index]==num:
        pass
    else:
        j=0
        while table[(index+j)%len(table)] != num:
            j+=1
            count+=1
    return count

if __name__ == '__main__':
    n=int(input())              #
    ht=[None]*n

    li=list(map(int,input().split()))
    num = int(input())

    add(ht,li)
    print(ht)
    print(search(ht,num))
