# 15686 치킨 배달

from itertools import combinations

n, m = map(int, input().split())

cities = [list(map(int, input().split())) for _ in range(n)]
res = 99999

chicken = []
home = []


for i in range(n):
    for j in range(n):
        if cities[i][j] == 1:
            home.append([i, j])
        elif cities[i][j] == 2:
            chicken.append([i, j])

chicken_picked = list(combinations(chicken, m))

for chick in chicken_picked:
    tmp = 0
    for h in home:
        tmpChick = 99999
        for c in chick:

            tmpChick = min(abs(h[0] - c[0]) + abs(h[1] - c[1]), tmpChick)
        tmp += tmpChick
    res = min(tmp, res)

print(res)
