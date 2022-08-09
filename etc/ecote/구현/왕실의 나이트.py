data = input()
row = int(data[1])
col = int(int(ord(data[0])) - int(ord("a"))) + 1

steps = [[2, -1], [2, 1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

res = 0
for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]
    if 1 <= nrow <= 8 and 1 <= ncol <= 8:
        res += 1

print(res)
