# 2630 색종이 만들기

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

blue = 0
white = 0


def recursion(x, y, n):
    global blue, white
    now_color = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):

            # 틀렸을 시 이 종이는 망한거라서 다시 분할정복을 함
            if now_color != board[i][j]:
                recursion(x, y, n // 2)  # 2사분면
                recursion(x + n // 2, y, n // 2)  # 3사분면
                recursion(x, y + n // 2, n // 2)  # 1사분면
                recursion(x + n // 2, y + n // 2, n // 2)  # 4사분면
                return

    if board[x][y] == 1:
        blue += 1
    else:
        white += 1


recursion(0, 0, n)
print(white)
print(blue)
