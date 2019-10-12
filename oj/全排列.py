result=[]
def full_permutation(list,k,n):
    """
一般把1~n这n个整数按某个顺序摆放的结果称为这n个整数的一个排列，而全排列指这n个整数能形成的所有排列。
例如对1、2、3这三个整数来说，(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)就是1~3的全排列，
该题输入一个数n，输出1~n的全排列

固定一个数，让其与后面的每个数交换，并一直递归到它被交换到最后一位，然后开始输出
把每个数固定一次，完成一次上面的过程
    """
    item=[]
    if k==n:
        for i in range(n+1):
            item.append(list[i])
        result.append(item)
    else:
        for i in range(k,n+1):
            list[i],list[k]=list[k],list[i]
            full_permutation(list,k+1,n)
            list[i], list[k] = list[k], list[i]     #把k换回原来的位置
    return result
list=[]
n=int(input())
for i in range(1,n+1):
    list.append(i)
list=full_permutation(list,0,len(list)-1)

dic={}                       #以下是排序的方法：存到字典中，用sorted排序
j=0
for i in list:
    dic[j]=i
    j+=1

dic=sorted(dic.values())
for i in dic:
    print(i)

