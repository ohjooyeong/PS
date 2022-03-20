# Sort 마스터 배지훈의 후계자 20551 백준

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr_a = []


for i in range(n):
    arr_a.append(int(input()))

arr_b = sorted(arr_a)

for i in range(m):
    num = int(input())
    lt = 0
    rt = len(arr_b)

    while lt < rt:
        mid = (lt + rt) // 2
        if arr_b[mid] >= num:
            rt = mid
        else:
            lt = mid + 1
    if 0 <= lt < n and arr_b[lt] == num:
        print(lt)
    else:
        print(-1)
