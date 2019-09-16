def quick_sort(list):
    if len(list)<=1:
        return list
    else:
        pivot=list.pop()            #随机选一个中间值
        left,right=[],[]
        for ele in list:
            if ele<pivot:
                left.append(ele)
            else:
                right.append(ele)
        return quick_sort(left)+[pivot]+quick_sort(right)


list=[17,45,2,78,12,664,0,8,33]
print(quick_sort(list))
