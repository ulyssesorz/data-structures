def plus(list):
    num = 0
    result=[]
    for i in range(len(list)):
        num += list.pop() * pow(10, i)    #转化为数字
    for i in str(num+1):                  #转化为列表
        result.append(i)
    result=[int(i) for i in result]
    return result

list=input().split()
list=[int(i) for i in list]
print(plus(list))



