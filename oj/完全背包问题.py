def bag(n, c, w, v):
	dp = [0 for i in range(c + 1)]
	for i in range(n):
		for j in range(w[i],c + 1):
				dp[j]=max(dp[j],dp[j-w[i]]+v[i])
	print(dp[-1])

if __name__ == '__main__':
	n = int(input())  # 物品的数量
	c = int(input())  # 背包的重量
	w = list(map(int, input().split()))
	v = list(map(int, input().split()))
	bag(n,c,w,v)