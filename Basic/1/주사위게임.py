n = int(input())
tot = []

for i in range(n):
    x, y, z = map(int, input().split())
    sum = 0
    if x == y and y == z:
        sum = 10000 + 1000 * x
    elif x == y or y == z or x == z:
        if x == y:
            sum = 1000 + 100 * x
        elif y == z:
            sum = 1000 + 100 * y
        else:
            sum = 1000 + 100 * x
    else:
        sum = max(x, y, z) * 100
    tot.append(sum)

print(max(tot))
