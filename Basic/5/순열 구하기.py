n, m = map(int, input().split())
ch = [0] * (n + 1)
res = [0] * m
cnt = 0

def dfs(L):
    global cnt
    if L == m:
        for i in res:
            print(i, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                dfs(L + 1)
                ch[i] = 0

dfs(0)

print(cnt)