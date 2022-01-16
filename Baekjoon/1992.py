# 쿼드트리 1992

N = int(input())

board = [list(map(int, input())) for _ in range(N)]


def recursion(x, y, n):
    check = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]:
                print("(", end="")
                recursion(x, y, n // 2)  # 2사분면
                recursion(x, y + n // 2, n // 2)  # 1사분면
                recursion(x + n // 2, y, n // 2)  # 3사분면
                recursion(x + n // 2, y + n // 2, n // 2)  # 4사분면
                print(")", end="")
                return
    print(check, end="")


recursion(0, 0, N)
