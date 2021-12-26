# 가장 긴 증가하는 부분 수열 4 14002
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
arr = arr[::-1]

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if arr[j] > arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

answer_arr = []
cnt = max(dp)
arr = arr[::-1]
dp = dp[::-1]

for i in range(n):
    if cnt == dp[i]:
        answer_arr.append(arr[i])
        cnt -= 1

print(max(dp))  # 길이
# 증가 배열
for num in answer_arr:
    print(num, end=" ")
print()
