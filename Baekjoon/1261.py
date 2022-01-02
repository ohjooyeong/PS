# 알고스팟 1261

from collections import deque


n, m = map(int, input().split())

board = [list(map(int, input())) for _ in range(m)]
dis = [[-1] * n for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append([0, 0])
dis[0][0] = 0  # 초기 시작 가중치 설정


def checkIndex(x, y):
    if 0 <= x < m and 0 <= y < n:
        return True
    return False


while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if checkIndex(nx, ny):
            if dis[nx][ny] == -1:
                if board[nx][ny] == 0:
                    dis[nx][ny] = dis[x][y]
                    q.appendleft([nx, ny])
                else:
                    dis[nx][ny] = dis[x][y] + 1
                    q.append([nx, ny])

print(dis[m - 1][n - 1])
