# 3020 개똥벌레

import sys

input = sys.stdin.readline

n, h = map(int, input().split())

top = []
bottom = []
ans = 2147483645

for i in range(n):
    k = int(input())
    if i % 2 == 0:
        bottom.append(k)
    else:
        top.append(k)

top.sort()
bottom.sort()


def check_stone(h, arr):
    lt, rt = 0, len(arr) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if arr[mid] <= h:
            lt = mid + 1
        else:
            rt = mid - 1
    return len(arr) - (rt + 1)


cnt = 0

for i in range(1, h + 1):
    bottom_cnt = check_stone(i - 1, bottom)
    top_cnt = check_stone(h - i, top)
    total_cnt = bottom_cnt + top_cnt

    if total_cnt < ans:
        cnt = 1
        ans = total_cnt
    elif total_cnt == ans:
        cnt += 1

print(ans, cnt)
