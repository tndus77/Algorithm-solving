n = int(input())
dp = [0] * 1001

dp[1] = 1 #n=1
dp[2] = 3 #n=2
dp[3] = 5 #n=3

for i in range(4, n+1):
  dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

print(dp[n])