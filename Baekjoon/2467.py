# 용액 2467 백준

import sys, math

input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))

lt = 0
rt = n - 1

comp = math.inf
ans = []
while lt < rt:
    if abs(sol[lt] + sol[rt]) < comp:
        comp = abs(sol[lt] + sol[rt])
        ans = [sol[lt], sol[rt]]

    if (sol[lt] + sol[rt]) < 0:
        lt += 1
    else:
        rt -= 1

print(*ans)
