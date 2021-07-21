# 스도쿠 2580 백준

import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
arr = []


for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            arr.append([i, j])

L = len(arr)


def row_check(x, v):
    if v in board[x]:
        return False
    return True


def col_check(y, v):
    for i in range(9):
        if v == board[i][y]:
            return False
    return True


def threeByThree(x, y, v):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if v == board[nx + i][ny + j]:
                return False
    return True


def dfs(cnt):
    if L == cnt:
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" ")
            print()
        sys.exit(0)
    else:
        for i in range(1, 10):
            nx = arr[cnt][0]
            ny = arr[cnt][1]

            if row_check(nx, i) and col_check(ny, i) and threeByThree(nx, ny, i):
                board[nx][ny] = i
                dfs(cnt + 1)
                board[nx][ny] = 0


dfs(0)
