from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    col, point, num = map(int, input().split())
    dq = deque(arr[col - 1])
    if point == 0:
        dq.rotate(-num)
    else:
        dq.rotate(num)
    arr[col - 1] = list(dq)

lt = 0
rt = n
mid = (lt + rt) // 2
res = 0
for i in range(n):
    res += sum(arr[i][lt:rt])
    if i < mid:
        lt += 1
        rt -= 1
    else:
        lt -= 1
        rt += 1

print(res)
