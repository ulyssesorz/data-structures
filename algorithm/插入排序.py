def insertion_sort(list,n):
    if n>0:
        insertion_sort(list,n-1)
        j=n-1
        while list[j]<list[j-1] and j>0:
            list[j],list[j-1]=list[j-1],list[j]      #向前比较，插入到合适位置
            j-=1
        return list
    else:
        return


list=[17,45,2,78,12,664,0,8,33]
print(insertion_sort(list,len(list)))
