"""
找零钱问题
输入硬币面值和要找的零钱数
输出需找最少硬币的数量，及硬币的搭配方式
"""
def coin(list, amount):
	n=len(list)
	max=99999
	last=[0]*(amount+1)         #初始化最后使用的硬币
	dp=[[max for i in range(amount+1)] for j in range(n+1)]
	for i in range(n+1):
		for j in range(amount+1):
			if i==0:            #初始化第一行
				dp[i][j]=max
			elif j==0:
				dp[i][j]=0      #初始化第一列
			else:
				dp[i][j] = dp[i - 1][j]
				if j>=list[i - 1] and dp[i][j - list[i - 1]] + 1<dp[i-1][j]:
					dp[i][j]=dp[i][j-list[i-1]]+1
					last[j]=list[i-1]           #记录使用的硬币价值
	print(dp[-1][-1])

	used_coin=[]
	while amount>0:
		used_coin.append(last[amount])
		amount-=last[amount]
	print(used_coin)


if __name__ == '__main__':
	list=list(map(int,input().split()))
	amount=int(input())
	coin(list,amount)