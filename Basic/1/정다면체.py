n, m = map(int, input().split())
best = [0] * (n + m + 1)
ans = []

for i in range(1, n + 1):
    for j in range(1, m + 1):
        best[i + j] += 1

maxValue = max(best)

for idx, v in enumerate(best):
    if maxValue == v:
        ans.append(idx)

print(ans)
