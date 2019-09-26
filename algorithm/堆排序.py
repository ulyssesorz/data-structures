def heapify(unsort,index,size):
    largest=index
    left=2*index+1
    right=2*index+2

    if left<size and unsort[left]>unsort[largest]:                           #建最大堆的过程
        largest=left
    if right < size and unsort[right] > unsort[largest]:
        largest = right
    if largest!=index:
        unsort[index],unsort[largest]=unsort[largest],unsort[index]
        heapify(unsort,largest,size)

def heap_sort(collection):
    n=len(collection)
    for i in range(n//2-1,-1,-1):                                   #遍历每个父节点，对其建堆，最终构造一个最大堆
        heapify(collection,i,n)
    for i in range(n-1,0,-1):
        collection[i],collection[0]=collection[0],collection[i]          #将最大值与最后一个值交换，并对除最后一个节点（最大）的其余节点构造堆
        heapify(collection,0,i)                                          #将size设置为i，目的是排除最后的n-i个节点(已排序)
    return collection

list=[13,56,4,2,134,33]
print(heap_sort(list))

