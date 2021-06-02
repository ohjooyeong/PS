# 교육과정 설계

from collections import deque

dq = list(input())
n = int(input())


for i in range(n):
    tmpdq = deque(dq)
    arr = list(input())
    for s in arr:
        if tmpdq and (s in tmpdq):
            if tmpdq[0] == s:
                tmpdq.popleft()
            else:
                print(f"#{i + 1} NO")
                break
    else:
        if tmpdq:
            print(f"#{i + 1} NO")
        else:
            print(f"#{i + 1} YES")
