arr = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
rotArr = list(map(list, zip(*arr)))

for i in range(7):
    for j in range(3):
        tmp = arr[i][j : j + 5]
        tmp2 = rotArr[i][j : j + 5]
        if tmp == tmp[::-1]:
            cnt += 1
        if tmp2 == tmp2[::-1]:
            cnt += 1
        # for k in range(2):
        #     if board[i+k][j] != board[i+5 - k - 1][j]:
        #         break
        # else:
        #     cnt += 1

print(cnt)
