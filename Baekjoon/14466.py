# 소가 길을 건너간 이유 6

import sys
from collections import deque

input = sys.stdin.readline

n, k, r = map(int, input().split())

road = [[[] for _ in range(n)] for _ in range(n)]
cow_board = [[0] * n for _ in range(n)]
cow_on = []

for i in range(r):
    r, c, rr, cc = map(int, input().split())
    road[r - 1][c - 1].append([rr - 1, cc - 1])
    road[rr - 1][cc - 1].append([r - 1, c - 1])


for i in range(k):
    r, c = map(int, input().split())
    cow_on.append([r - 1, c - 1])
    cow_board[r - 1][c - 1] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


answer = 0
for r, c in cow_on:
    if cow_board[r][c]:
        visited = [[0] * n for _ in range(n)]
        q = deque()
        q.append([r, c])
        cow_board[r][c] = 0
        cnt = 0
        k -= 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if [nx, ny] not in road[x][y]:
                        q.append([nx, ny])
                        visited[nx][ny] = 1
                        if cow_board[nx][ny]:
                            cnt += 1
        answer += k - cnt

print(answer)
