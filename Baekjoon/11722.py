# 가장 긴 감소하는 부분 수열 11722

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if arr[j] > arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
