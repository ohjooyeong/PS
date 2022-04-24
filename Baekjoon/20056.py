# 20056 마법사 상어와 파이어볼

import sys
from copy import deepcopy

input = sys.stdin.readline

N, M, K = map(int, input().split())

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

board = [[[] for _ in range(N)] for _ in range(N)]

tmp_board = [[[] * N] * N for _ in range(N)]


for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    if m != 0:
        board[r - 1][c - 1].append([m, s, d])


for _ in range(K):
    tmp_board = [[[] for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if board[x][y] != []:
                fire_len = len(board[x][y])
                for f in range(fire_len):
                    nm, ns, nd = board[x][y][f]
                    nx, ny = x + dx[nd] * ns, y + dy[nd] * ns
                    nx = (nx + N) % N
                    ny = (ny + N) % N
                    tmp_board[nx][ny].append([nm, ns, nd])

    for x in range(N):
        for y in range(N):
            fire_len = len(tmp_board[x][y])
            if fire_len > 1:
                total_m, total_s, total_d = 0, 0, []
                for f in range(fire_len):
                    total_m += tmp_board[x][y][f][0]
                    total_s += tmp_board[x][y][f][1]
                    total_d.append(tmp_board[x][y][f][2] % 2)
                total_m = int(total_m / 5)
                total_s = int(total_s / fire_len)
                tmp_board[x][y] = []

                if total_m != 0:
                    if sum(total_d) == 0 or sum(total_d) == fire_len:
                        for i in range(4):
                            tmp_board[x][y].append([total_m, total_s, i * 2])
                    else:
                        for j in range(4):
                            tmp_board[x][y].append([total_m, total_s, j * 2 + 1])

    board = deepcopy(tmp_board)


sum_m = 0
for x in range(N):
    for y in range(N):
        if board[x][y] != []:
            for b in range(len(board[x][y])):
                sum_m += board[x][y][b][0]

print(sum_m)
