def selection_sort(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]        #i位置的数和后面的数比较，大则交换
    return list

list=[17,45,2,78,12,664,0,8,33]
print(selection_sort(list))
