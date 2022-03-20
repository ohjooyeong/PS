# 문자열 게임 20437 백준

import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())


def solution(w, k, dic):
    flag = 0
    arr = []
    gap = []
    for i, s in enumerate(w):
        dic[s] += [i]
    for key, v in dic.items():
        if len(v) >= k:
            flag = 1
            arr.append(v)
    if not flag:
        return [-1]

    for a in arr:
        for i in range(len(a) - k + 1):
            gap.append(a[i + k - 1] - a[i])
    return [min(gap) + 1, max(gap) + 1]


for i in range(T):
    str_dict = defaultdict(list)
    w = input().strip()
    k = int(input())
    ans = solution(w, k, str_dict)
    if ans[0] == -1:
        print(-1)
    else:
        print(f"{ans[0]} {ans[1]}")
