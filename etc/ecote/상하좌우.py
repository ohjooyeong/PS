from asyncio import constants


n = int(input())
trip = input().split()

direct = {"L": [-1, 0], "R": [1, 0], "U": [0, -1], "D": [0, 1]}

x = 1
y = 1

for t in trip:
    nx = direct[t][0] + x
    ny = direct[t][1] + y

    print(nx, ny, direct[t])

    if 1 <= nx <= n and 1 <= ny <= n:
        x = nx
        y = ny

print(y, x)
