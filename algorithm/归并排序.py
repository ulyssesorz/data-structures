def merge_sort(list):
    def merge(left,right):
        result=[]
        while left and right:
            result.append((left if left[0]<right[0] else right).pop(0))    #从排好序的子列选较小的元素放入result
        return result+left+right

    if len(list)<=1:                                                       #merge_sort分，merge排序合并
        return list
    else:
        mid=len(list)//2
        left=list[:mid]
        right=list[mid:]
        return merge(merge_sort(left),merge_sort(right))

list=[17,45,2,78,12,664,0,8,33]
print(merge_sort(list))
