n = int(input())

player = []

for i in range(n):
    h, w = map(int, input().split())
    player.append([h, w])

player.sort(reverse=True)

cnt = 1
comp = player[0][1]

for i in range(1, n):
    if comp < player[i][1]:
        comp = player[i][1]
        cnt += 1

print(cnt)
