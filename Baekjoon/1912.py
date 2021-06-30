# 연속합 1912

n = int(input())
dp = [0] * n
arr = list(map(int, input().split()))

res = -1001
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

print(max(dp))
