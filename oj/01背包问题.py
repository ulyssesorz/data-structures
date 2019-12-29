"""
第一行输入一个正整数n，表示共有n个商品，每个商品依次编号为1,2，…，n；第二行输入一个正整数c，
表示背包的重量为c；第三行按从小到大的商品编号顺序依次输入每个商品的重量，重量为正整数，元素之间以空格隔开；
第四行按从小到大的商品编号顺序依次输入每个商品的价格，价格也为正整数，元素之间以空格隔开。

第一行输出背包的最高总价格，第二行按从小到大的顺序输出选中的商品编号，元素间以空格隔开。
"""


def bag(n, c, w, v):
	global li
	dp = [[0 for j in range(c + 1)] for i in range(n + 1)]
	for i in range(1, n + 1):
		for j in range(1, c + 1):
			dp[i][j] = dp[i - 1][j]  # 第一种情况，不选i（默认）
			if j >= w[i - 1] and dp[i][j] < dp[i - 1][j - w[i - 1]] + v[i - 1]:  # 第二种，背包容量足够且选i有更大收益，选i
				dp[i][j] = dp[i - 1][j - w[i - 1]] + v[i - 1]
	return dp

def show(n, c, w, dp):
	print(dp[n][c])  # 输出最后一种情况的最大重量时的收益
	x = [False for i in range(n)]  # 表示每种物品
	j = c
	for i in range(n, 0, -1):
		if dp[i][j] > dp[i - 1][j]:  # 收益更大，说明选了第i个物品
			x[i - 1] = True
			j -= w[i - 1]
	for i in range(n):
		if x[i]:
			print(i + 1, end=' ')


if __name__ == '__main__':
	n = int(input())  # 物品的数量
	c = int(input())  # 背包的重量
	w = list(map(int, input().split()))
	v = list(map(int, input().split()))
	show(n, c, w, bag(n, c, w, v))

"""
如果只需得出价值
标准的01背包解法:
def bag(n, c, w, v):
	dp = [0 for i in range(c + 1)]
	for i in range(n):
		for j in range(c,-1,-1):
			if j>=w[i]:
				dp[j]=max(dp[j],dp[j-w[i]]+v[i])
	print(dp[-1])

if __name__ == '__main__':
	n = int(input())  # 物品的数量
	c = int(input())  # 背包的重量
	w = list(map(int, input().split()))
	v = list(map(int, input().split()))
	bag(n,c,w,v)
"""