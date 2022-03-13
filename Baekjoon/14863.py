# 서울에서 경산까지 14863 백준
import sys

# 틀림 왜 틀린지 찾아야함
input = sys.stdin.readline

n, K = map(int, input().split())

dp = [[-1] * (100001) for _ in range(101)]
trip = []
for i in range(n):
    trip.append(list(map(int, input().split())))


dp[0][trip[0][0]] = trip[0][1]
dp[0][trip[0][2]] = trip[0][3]

result = 0


for i in range(1, n):
    for k in range(K + 1):
        # 전 도시도 안밟은 경우
        if dp[i - 1][k] == -1:
            continue

        # 도보
        if (k + trip[i][0]) <= K:
            dp[i][k + trip[i][0]] = max(dp[i][k + trip[i][0]], dp[i - 1][k] + trip[i][1])
            result = max(result, dp[i][k + trip[i][0]])

        # 자전거
        if (k + trip[i][2]) <= K:
            dp[i][k + trip[i][2]] = max(dp[i][k + trip[i][2]], dp[i - 1][k] + trip[i][3])
            result = max(result, dp[i][k + trip[i][2]])

print(result)
