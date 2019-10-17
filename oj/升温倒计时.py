def tem(list):
    """
    输入一组温度数据，输出一组数据，该输出数据对应位置的数据是对应位置的输入数据需要再等待多久温度才会升高的天数。
    如果之后都不会升高，请输入 0 来代替。例如输入一组数据12 31 23 22 22 35 34，则输出数据是[1,4,3,2,1,0,0]。
    """
    result=[]
    for i in range(len(list)-1):
        j=i
        while list[j+1]<=list[i]:     #遍历每个元素，和后面的元素比较大小
            j+=1
            if j==len(list)-1:        #防止溢出
                break
        if j==len(list)-1:            #处理倒数第二个值
            result.append(0)
        else:
            result.append(j-i+1)
    result.append(0)                  #补齐最后一个值

    return result

list=input().split()
list=[int(i) for i in list]
print(tem(list))