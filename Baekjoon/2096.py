# 내려가기 2096 백준

import sys

input = sys.stdin.readline
arr = []

n = int(input())

max_dp = [0 for _ in range(3)]
min_dp = [0 for _ in range(3)]

for _ in range(n):
    a, b, c = map(int, input().split())

    tmp_a_max = max(max_dp[0], max_dp[1]) + a
    tmp_b_max = max(max_dp[0], max_dp[1], max_dp[2]) + b
    tmp_c_max = max(max_dp[1], max_dp[2]) + c

    tmp_a_min = min(min_dp[0], min_dp[1]) + a
    tmp_b_min = min(min_dp[0], min_dp[1], min_dp[2]) + b
    tmp_c_min = min(min_dp[1], min_dp[2]) + c

    max_dp = [tmp_a_max, tmp_b_max, tmp_c_max]
    min_dp = [tmp_a_min, tmp_b_min, tmp_c_min]

print(max(max_dp), min(min_dp))
