def func(num):
    """
    给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。
    如果没有两个连续的 1（即该二进制数只有一个1），返回 0 。
    """
    count = 0
    list = []
    while num != 1 and num != 0:
        list.append(num % 2)
        num //= 2
        count += 1
    list.append(num)
    count += 1
    result = 0
    for j in range(1, count + 1):
        result = result + list.pop() * (pow(10, (count - j)))
    return result                                                #十进制转化为二进制

n = int(input())
items=[]
res=[]
k=0
for i in str(func(n)):               #转化为字符串
    items.append(i)
for i in range(len(items)):
    if items[i]=='1':                #找到1时开始向后找
        j=i+1
        if j<len(items):             #防止越界
            while items[j]!='1':
                k+=1
                j+=1
                if j>=len(items):    #防止越界
                    break
            if j<len(items):         #避免时结尾为0的情况，如101000，此时最后一段不算距离
                res.append(k)
            k=0
            j=0

if len(res)==0:
    print('0')
else:
    print(max(res)+1)






