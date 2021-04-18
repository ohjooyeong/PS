n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    board[i].append(0)
    board[i].insert(0, 0)

board.insert(0, [0] * (n + 2))
board.append([0] * (n + 2))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt = 0
for j in range(1, n + 1):
    for k in range(1, n + 1):
        for m in range(4):
            if board[j + dy[m]][k + dx[m]] >= board[j][k]:
                break
        else:
            cnt += 1

print(cnt)
