# 5430 AC
from collections import deque

T = int(input())


for i in range(T):
    funcArr = input()
    arrLeng = int(input())

    arr = input()[1:-1].split(",")
    ans = ""

    if arrLeng == 0:
        arr = []
    arr = deque(arr)

    revCnt = 0

    for f in funcArr:
        if f == "R":
            revCnt += 1
        else:
            if len(arr) == 0:
                ans = "error"
                break
            else:
                if revCnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if ans == "":
        if revCnt % 2 == 1:
            arr.reverse()
        tmp = ",".join(arr)
        ans = f"[{tmp}]"

    print(ans)
