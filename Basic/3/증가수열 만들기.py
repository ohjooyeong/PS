n = int(input())
from collections import deque

arr = list(map(int, input().split()))
arr = deque(arr)

prev = -1
ans = ""
lt = 0
rt = 0
tmp = []
while arr:
    lt = [arr[0], "L"]
    rt = [arr[-1], "R"]
    if lt[0] > prev:
        tmp.append(lt)
    if rt[0] > prev:
        tmp.append(rt)
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        ans += tmp[0][1]
        prev = tmp[0][0]
        if tmp[0][1] == "L":
            arr.popleft()
        else:
            arr.pop()
    tmp = []

print(len(ans))
print(ans)
