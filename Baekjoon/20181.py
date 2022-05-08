# 꿈틀꿈틀 호석 애벌레 백준 20181

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

lt, rt, sum_value = 0, 0, 0
dp = [0] * (len(arr) + 1)

while rt <= n:
    if sum_value >= k:
        while sum_value >= k:
            dp[rt] = max(dp[rt], dp[lt] + sum_value - k)
            sum_value -= arr[lt]
            lt += 1
    else:
        dp[rt] = max(dp[rt], dp[rt - 1])

        if rt == n:
            break

        sum_value += arr[rt]
        rt += 1

print(dp[n])

# dp
# 다이나믹 프로그래밍
# 투포인터
# 누적합
