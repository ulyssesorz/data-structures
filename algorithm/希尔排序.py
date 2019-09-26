def shell_sort(collection):
    n=len(collection)
    gap=n//2                         #设置希尔序列：偶数（以及1）

    while gap>0:
        for i in range(gap,n):
            temp=collection[i]
            j=i
            while j>=gap and collection[j-gap]>temp:      #插入排序
                collection[j]=collection[j-gap]           
                j-=gap
            collection[j]=temp
        gap//=2                                           #缩小间隔
    return collection

list=[34,12,7,80,34,124,66,9]
print(shell_sort(list))