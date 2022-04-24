# 21278 호석이 두마리 치킨

import sys

# https://it-garden.tistory.com/247 플로이드 와샬 참고

INF = sys.maxsize

input = sys.stdin.readline

n, m = map(int, input().split())

dist = [[INF] * n for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0


for i in range(m):
    x, y = map(int, input().split())
    dist[x - 1][y - 1] = 1
    dist[y - 1][x - 1] = 1

# 플로이드 와샬 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 두 개의 치킨집을 가정
# 모든 건물들과의 최소값 브루트 포스
minValue = INF
for i in range(n):
    for j in range(n):
        sum_dist = 0
        for k in range(n):
            sum_dist += min(dist[k][i], dist[k][j])
        if minValue > sum_dist * 2:
            minValue = sum_dist * 2
            ans = [i + 1, j + 1, minValue]

print(*ans)
