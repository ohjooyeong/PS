# 비숍 1799 백준

import sys

input = sys.stdin.readline
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
black = []
white = []
color = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        color[i][j] = (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)

for i in range(n):
    for j in range(n):
        if color[i][j] == True and board[i][j] == 1:
            black.append([i, j])
        if color[i][j] == False and board[i][j] == 1:
            white.append([i, j])

cnt_black = 0
cnt_white = 0

is_used_x = [0] * (n * 2 - 1)
is_used_y = [0] * (n * 2 - 1)


def dfs(chess_mal, index, cnt):
    global cnt_black, cnt_white
    if len(chess_mal) == 0:
        return
    if index == len(chess_mal):
        xx, yy = chess_mal[index - 1]
        if color[xx][yy]:
            cnt_black = max(cnt_black, cnt)
        else:
            cnt_white = max(cnt_white, cnt)
        return

    x, y = chess_mal[index]
    if is_used_x[x + y] or is_used_y[x - y + n - 1]:
        dfs(chess_mal, index + 1, cnt)
    else:
        is_used_x[x + y] = 1
        is_used_y[x - y + n - 1] = 1
        dfs(chess_mal, index + 1, cnt + 1)
        is_used_x[x + y] = 0
        is_used_y[x - y + n - 1] = 0
        dfs(chess_mal, index + 1, cnt)


dfs(black, 0, 0)
dfs(white, 0, 0)

print(cnt_black + cnt_white)
