# 색종이와 가위 20444 백준

import sys

input = sys.stdin.readline

n, k = map(int, input().split())


def solution(lt, rt):
    while lt <= rt:
        mid = (lt + rt) // 2
        value = (mid + 1) * (n - mid + 1)
        if value == k:
            print("YES")
            return
        if value > k:
            rt = mid - 1
        else:
            lt = mid + 1
    print("NO")
    return


solution(0, n)
