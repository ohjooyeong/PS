# 내리막 길 1520

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and board[x][y] > board[nx][ny]:
            cnt += dfs(nx, ny)

    dp[x][y] = cnt
    return dp[x][y]


print(dfs(0, 0))

# 런타임 에러(NameError)
# dp와 같이 풀어야 했음. 답 봄

# input = sys.stdin.readline

# n, m = map(int, input().split())

# board = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
# cnt = 0
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]


# def dfs(x, y):
#     global cnt
#     if x == n - 1 and y == m - 1:
#         cnt += 1
#         return
#     else:

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (
#                 0 <= nx <= n - 1
#                 and 0 <= ny <= m - 1
#                 and visited[nx][ny] == 0
#                 and board[x][y] > board[nx][ny]
#             ):
#                 visited[x][y] = 1
#                 dfs(nx, ny)
#                 visited[x][y] = 0


# dfs(0, 0)
# print(cnt)
