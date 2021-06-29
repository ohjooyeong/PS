c, n = map(int, input().split())
a = []
result = -214700000


def dfs(L, sum, tsum):
    global result, total
    if sum + (total - tsum) < result:
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        dfs(L + 1, sum + a[L], tsum + a[L])
        dfs(L + 1, sum, tsum + a[L])


for _ in range(n):
    tmp = int(input())
    a.append(tmp)

total = sum(a)

dfs(0, 0, 0)

print(result)
