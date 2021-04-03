# 백준 분수찾기

x = int(input())

level = 0
sum1 = 0

while sum1 < x:
    level += 1
    sum1 = sum1 + level

div = sum1 + 1 - x

if level % 2 == 0:
    up = level + 1 - div
    down = div
    print("{}/{}".format(up, down))
else:
    up = div
    down = level + 1 - div
    print("{}/{}".format(up, down))
