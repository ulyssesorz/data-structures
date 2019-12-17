"""
给定一个正整数集合X={x1,x2,…,xn}，设计回溯算法，判断是否存在子集Y，使得Y中元素之和等于集合元素总和的一半。
"""
def backtrack(i,valsum):
	global flag             #定义全局变量，以便修改flag的值
	if i>=n:                #超出集合，退出递归
		return
	valsum+=set[i]          #valsum为当前的元素和
	if valsum==s:           #满足题目条件
		flag=1
		return
	elif valsum<s:                  #小于一半，递归，继续处理下一个数
		backtrack(i+1,valsum)
	valsum-=set[i]                  #当valsum大于s时，回溯，减去当前值，回到上一中情况
	backtrack(i+1,valsum)        #继续递归处理下下个数

if __name__ == '__main__':
	set=list(map(int, input().split()))
	s= sum(set) // 2
	n=len(set)
	flag=0
	backtrack(0,0)
	if flag==1:
		print('True')
	else:
		print('False')