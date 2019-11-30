n,m  = map(int, input().split())
INF = 1000000007
broken_stairs = set([int(input()) for i in range(m)])

dp = [0] * (n + 1)
dp[0] = 1
if 1 not in broken_stairs:
	dp[1] = 1
else:
	dp[1] = 0
for i in range(2, n + 1):
	if i in broken_stairs:
		continue
	dp[i] = dp[i - 1] + dp[i - 2]
	dp[i] %= INF
print(dp[n])
