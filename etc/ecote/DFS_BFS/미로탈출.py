from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

q = deque([])
q.append((0, 0))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


while q:
    x, y = q.popleft()
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and board[nx][ny] == 1:
            q.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

print(board[n - 1][m - 1])
