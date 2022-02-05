# 경주로 건설 67259

import math
from collections import deque


def solution(board):
    n = len(board)
    dirs = [[-1, 0, 0], [0, 1, 1], [1, 0, 2], [0, -1, 3]]
    dp = [[math.inf] * n for _ in range(n)]
    q = deque()
    q.append([0, 0, 0, -1])
    while q:
        x, y, cost, dir_idx = q.popleft()

        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            add_cost = 6
            if dir_idx == dir[2] or dir_idx == -1:
                add_cost = 1

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if dp[nx][ny] < cost + add_cost - 4:
                    continue
                dp[nx][ny] = cost + add_cost
                q.append([nx, ny, cost + add_cost, dir[2]])

    return dp[n - 1][n - 1] * 100


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
)
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
