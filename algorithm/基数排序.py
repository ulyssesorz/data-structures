def radix_sort(collection):
    i=0
    maxnum=max(collection)
    j=len(str(maxnum))                                 #j是最大数的最高位数
    while i<j:
        bucket=[[] for i in range(10)]                 #分出10个桶
        for x in collection:
            bucket[int(x/(10**i)%10)].append(x)        #排i+1位，向桶中添加数
        collection.clear()
        for x in bucket:                               #按顺序放回原桶
            for y in x:
                collection.append(y)
        i+=1
    return collection

list=[15,78,34,2,89,122,21]
print(radix_sort(list))

