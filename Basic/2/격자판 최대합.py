n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0

for i in range(n):
    res = max(res, sum(arr[i][:]))
    tmp = 0
    for j in range(n):
        tmp += arr[j][i]
    res = max(res, tmp)

tmp = 0
for k in range(n):
    tmp += arr[k][k]
res = max(res, tmp)

tmp = 0
for k in range(n):
    tmp += arr[k][n - k - 1]
res = max(res, tmp)

print(res)
