import sys

n, m = map(int, input().split())

p = [0] * n
b = [1] * n
ch = [0] * (n + 1)

for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i

def dfs(L):
    if L == n:
        sum = 0
        for i in range(n):
            sum += p[i] * b[i]
        if sum == m:
            print(p)
            sys.exit(0)
        return
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                dfs(L + 1)
                ch[i] = 0

dfs(0)

print(p)