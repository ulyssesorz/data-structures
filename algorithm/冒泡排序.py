def bubble_sort(collection):
    n=len(collection)
    for i in range(n-1,-1,-1):
        swap=False
        for j in range(i):
            if collection[j]>collection[j+1]:
                swap=True                                                     #标记，若此次for未交换，说明已排好序，无需再检查
                collection[j],collection[j+1]=collection[j+1],collection[j]
        if not swap:
            break
    return collection

list=[76,1,45,23,12,66,4]
print(bubble_sort(list))